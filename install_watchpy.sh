#!/usr/bin/env bash
mkdir $HOME/.local/share/watch_py
cd $HOME/.local/share/watch_py
curl -o watch.py https://raw.githubusercontent.com/dmmat/watch.py/master/watch.py
chmod +x watch.py

if [[ -f $HOME/.bashrc ]]; then
    if ! grep -Fxq 'export PATH="$PATH:$HOME/.local/share/watch_py"' $HOME/.bashrc; then
        echo "add watch py to .bashrc"
        echo '# add watch py to user run' >> $HOME/.bashrc
        echo 'export PATH="$PATH:$HOME/.local/share/watch_py"' >> $HOME/.bashrc
    fi
fi

if [[ -f $HOME/.zshrc ]]; then
    if ! grep -Fxq 'export PATH="$PATH:$HOME/.local/share/watch_py"' $HOME/.zshrc; then
        echo "add watch py to .zshrc"
        echo '# add watch py to user run' >> $HOME/.zshrc
        echo 'export PATH="$PATH:$HOME/.local/share/watch_py"' >> $HOME/.zshrc
    fi
fi

echo "reopen terminal or run export PATH=\"\$PATH:\$HOME/.local/share/watch_py\""
echo "installation done"