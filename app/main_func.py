import speedtest

st = speedtest.Speedtest()

def test_speed():
    download_speed = st.download()
    upload_speed = st.upload()
    server_names = []
    st.get_servers(server_names)
    ping = st.results.ping

    download_Mbs = convert_bytes(download_speed)
    upload_Mbs = convert_bytes(upload_speed)
    return download_Mbs, upload_Mbs, ping

def convert_bytes(speed):
    Mbs = speed / 1000000
    return Mbs