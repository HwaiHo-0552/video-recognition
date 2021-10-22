#/usr/bin/python
#-*- coding:UTF-8 -*-

import cv2

video_path = 'V:\\Coding\\timesformer\\vis_results\\vis_demo2.mp4'
video_name = 'V:\\Coding\\timesformer\\vis_results\\video_recognition.mp4'
predict = {'Walking':'75%', 'Handsome':'10-point', 'Character':'nice man'}
title_text = 'SAIL Lab'

class video_proc:
    def __init__(self, v_pth, v_name, title, preds):
        self.v_pth = v_pth
        self.v_name = v_name
        self.title = title
        self.preds = preds

    def get_video(self):
        cap = cv2.VideoCapture(self.v_pth)
        v_fps = cap.get(cv2.CAP_PROP_FPS)
        f_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        f_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

        return cap, v_fps, f_height, f_width

    def proc_video(self, v_cap, v_fps, f_height, f_width):
        v_encode = cv2.VideoWriter_fourcc(*'mp4v')
        save_video = cv2.VideoWriter(
                                    self.v_name, v_encode, v_fps, 
                                    ( int(f_width), int(f_height) )
                                    )
        while (v_cap.isOpened()):
            ret, frame = v_cap.read()
            if ret==True:
                new_f = cv2.putText(frame, self.title, (20, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,20), 2)
                for n, key in enumerate(self.preds):
                    x = int(20)
                    y = int(100+n*28)
                    content = key+':'+self.preds[key]
                    new_f = cv2.putText(frame, content, (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (200,0,0), 2)
                save_video.write(new_f)
            else:
                save_video.release()
                break

def main():
    v_p = video_proc(video_path, video_name, title_text, predict)
    cap, v_fps, f_height, f_width = v_p.get_video()
    v_p.proc_video(cap, v_fps, f_height, f_width)

    cap.release()

if __name__ == '__main__':
    main()