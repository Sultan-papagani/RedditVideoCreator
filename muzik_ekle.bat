ffmpeg -i final_video.mp4 -i arka_plan_muzigi.mp3 -filter_complex "[0:a][1:a]amerge=inputs=2[a]" -map 0:v -map "[a]" -c:v copy -ac 2 -shortest final_output_video.mp4
