CALL C:\mch_py_38\Scripts\activate.bat
echo %1
python ./zmq_fw.py worker tcp 127.0.0.1 5557 tcp 127.0.0.1 5558