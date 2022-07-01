#!/bin/bash
echo "how many times?"
read repeat
python -c "import trade; trade.goldbuy('sell',$repeat)"