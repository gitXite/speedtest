import speedtest

st = speedtest.Speedtest()

def test_speed():
    download_speed = st.download()
    upload_speed = st.upload()
    server_names = []
    st.get_servers(server_names)
    ping = st.results.ping

    download_Mb = convert_bytes(download_speed)
    upload_Mb = convert_bytes(upload_speed)

    return download_Mb, upload_Mb, ping

def convert_bytes(speed):
    Mbs = speed / 1000000
    return Mbs
