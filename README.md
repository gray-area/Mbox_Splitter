📬 MBOX Splitter

A fast and efficient Python tool for splitting large .mbox email archive files into smaller chunks. Designed to prevent issues with oversized mailbox files and improve email management.

🚀 Features

✅ Splits large .mbox files into smaller parts based on size (MB)
✅ Preserves email integrity and format
✅ Real-time progress tracking with a dynamic progress bar
✅ Automatically names output files sequentially (file_1.mbox, file_2.mbox, etc.)
✅ Works efficiently with large .mbox files

📌 Requirements

Make sure you have Python 3.x installed. Additionally, install the required dependencies:

pip install tqdm

📥 Installation

Clone the repository and navigate to the project folder:

git clone https://github.com/yourusername/mbox-splitter.git
cd mbox-splitter

🔧 Usage

Run the script with the following command:

python mbox-splitter.py <filename.mbox> <size_in_MB>

📌 Example

Splitting a backup.mbox file into 50MB chunks:

python mbox-splitter.py backup.mbox 50

📤 Output

The tool will generate new .mbox files in the same directory:

backup_1.mbox (≈ 50MB)
backup_2.mbox (≈ 50MB)
backup_3.mbox (remaining size)

You'll also see a progress bar tracking the email processing:

Processing Emails: 120/500 [#####-----]  40% Completed

🛠️ How It Works

Reads the .mbox file message by message.

Calculates each email’s size in bytes.

Writes messages into a new .mbox file until it reaches the specified size.

Creates a new .mbox file and continues processing.

🐍 Compatibility

✅ Python 3.x✅ Works on Windows, macOS, and Linux

🏆 Contributing

Feel free to fork this repo and submit a pull request! Any contributions, suggestions, or improvements are welcome.

📜 License

MIT License. See LICENSE for details.

📧 Contact

For questions or support, open an issue on GitHub or reach out to your-email@example.com.

🚀 Enjoy hassle-free .mbox splitting! 🎯
