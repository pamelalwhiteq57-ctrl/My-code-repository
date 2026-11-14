import requests

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36 Edg/157.0.0.0",
        "referer":"https://www.bilibili.com/video/BV1Ru4y1N7tY/?spm_id_from=333.1007.top_right_bar_window_custom_collection.content.click&vd_source=6e96dbcccbd2447caeb24da75f9d6f3c"
}

url = "https://upos-sz-mirrorcoso1.bilivideo.com/upgcxcode/38/64/1332976438/1332976438-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&deadline=1794325228&nbs=1&trid=47f3c588746f4cf7b62ea087d5094f0u&uipk=5&mid=516495843&oi=0x240e04763002030f155f239729e70d5d&platform=pc&gen=playurlv3&os=coso1bv&og=cos&upsig=64aeb464e2668f43223318f0551dcd5f&uparams=e,deadline,nbs,trid,uipk,mid,oi,platform,gen,os,og&bvc=vod&nettype=0&bw=722665&lrs=-1&V=v3.1.1.0&f=u_0_0&qn_dyeid=0f69680de24d9b7f002f33376af31ecc&agrr=0&buvid=1770F824-0A1A-F254-4869-C26731046E4C14912infoc&build=0&dl=0&orderid=0,3"

with requests.get(url, headers=headers, stream=True) as res:
    if res.status_code != 200:
        print("下载失败，状态码:", res.status_code)
    with open("视频.mp4", "wb") as f:
        for chunk in res.iter_content(chunk_size=8192):
            f.write(chunk)

url = "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/38/64/1332976438/1332976438-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&mid=516495843&trid=47f3c588746f4cf7b62ea087d5094f0u&og=hw&deadline=1794325228&nbs=1&oi=0x240e04763002030f155f239729e70d5d&platform=pc&gen=playurlv3&os=hwbv&uipk=5&upsig=65f5bdbb6dcc36a8c90da018806c641f&uparams=e,mid,trid,og,deadline,nbs,oi,platform,gen,os,uipk&bvc=vod&nettype=0&bw=105771&lrs=-1&V=v3.1.1.0&build=0&dl=0&f=u_0_0&qn_dyeid=0f69680de24d9b7f002f33376af31ecc&agrr=0&buvid=1770F824-0A1A-F254-4869-C26731046E4C14912infoc&orderid=0,3"

res = requests.get(url, headers=headers)

open("音频.mp3", "wb").write(res.content)

from moviepy.editor import *
video = VideoFileClip("视频.mp4")
audio = AudioFileClip("音频.mp3")

sp = video.set_audio(audio)
sp.write_videofile("Bilibili爬取的视频.mp4")