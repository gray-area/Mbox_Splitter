import mailbox
import sys
import os
from tqdm import tqdm  # Progress bar

if len(sys.argv) != 3:
    print("\nUsage: python mbox-splitter.py filename.mbox size")
    print("       where `size` is a positive integer in MB\n")
    sys.exit()

filename = sys.argv[1]
if not os.path.exists(filename):
    print(f"File `{filename}` does not exist.")
    sys.exit()

try:
    split_size = int(sys.argv[2]) * 1024 * 1024  # Convert MB to Bytes
except ValueError:
    print("Size must be a positive number")
    sys.exit()

if split_size < 1:
    print("Size must be a positive number")
    sys.exit()

chunk_count = 1
output = filename.replace('.mbox', f'_{chunk_count}.mbox')
if os.path.exists(output):
    print(f"The file `{filename}` has already been split. Delete chunks to continue.")
    sys.exit()

print(f"Splitting `{filename}` into chunks of {sys.argv[2]} MB...\n")

total_size = 0
message_count = 0
of = mailbox.mbox(output, create=True)

# Open the mbox file safely
mbox = mailbox.mbox(filename)

# Initialize tqdm with unknown total (fixes 0 messages issue)
pbar = tqdm(desc="Processing Emails", unit="msg", dynamic_ncols=True)

for message in mbox:  # Read messages dynamically
    message_count += 1
    message_size = len(message.as_string().encode('utf-8'))  # Accurate size in bytes

    if total_size + message_size >= split_size:
        of.close()
        print(f"Created file `{output}`, size={total_size // (1024 * 1024)}MB, messages={message_count}.")
        chunk_count += 1
        output = filename.replace('.mbox', f'_{chunk_count}.mbox')
        of = mailbox.mbox(output, create=True)
        total_size = 0
        message_count = 0

    of.add(message)
    total_size += message_size
    pbar.update(1)  # Update progress bar

of.close()
pbar.close()
print(f"Created file `{output}`, size={total_size // (1024 * 1024)}MB, messages={message_count}.")
print("\nDone.")
