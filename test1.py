import pyaudio
import pyrealsense2 as rs
import tensorflow as tf
import numpy as np
import cv2
import time

### CAMERA TEST ###
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 6)
pipeline.start(config)

while True:
    frame = pipeline.wait_for_frames()
    if frame is not None:
        color_frame = frame.get_color_frame()
        if color_frame is not None:
            print(np.asanyarray(color_frame.get_data()))
        else:
            print("error 2")
    else:
        print("error 1")

### RESPEAKER TEST ###
# class PyAudioSource():
#     '''PyAudioSource implements AudioSource through the use of the PyAudio library.
#     Opens a continuous stream from the microphone through PyAudio.
#     # Arguments
#         device_index: int
#             Microphone index: index in the list speech_recognition.Microphone.list_microphone_names()
#         sample_rate: float 
#             Sampling rate - `default 16000`
#         frames_per_buffer: int
#             Chunk size (in samples) - `default 1024`
#         channels: int / list
#             Number of channels - `default 1`
#         format: str
#             Audio array dtype: 'int16' or 'float32' - `default 'int16'`
        
#     For more details refer to the PyAudio library docs.
#     '''
#     def __init__(self,device_index=None, sample_rate=16000, channels=1, frames_per_buffer=1024, format='int16'):
#         self.device_index=device_index
#         self.sample_rate=sample_rate
#         self.channels=channels
#         self.frames_per_buffer=frames_per_buffer
#         self.format=format

#         # Create an instance of PyAudio
#         self.p = pyaudio.PyAudio()

#         # Open the audio stream
#         self.stream = self.p.open(      
#             output=False,  
#             rate=self.sample_rate,					   
#             format=pyaudio.paInt16 if format == 'int16' else pyaudio.paFloat32,		
#             channels=self.channels,				        
#             input=True,				        
#             input_device_index=self.device_index,	        
#             frames_per_buffer=self.frames_per_buffer,	
#             stream_callback=None		    
#         )
    
#     def get_audio_frame(self):
#         audio_data = self.stream.read(self.frames_per_buffer, exception_on_overflow=False)
#         audio_array = np.frombuffer(audio_data, dtype=np.int16 if self.format == 'int16' else np.float32)
        
#         return audio_array


#     def stop(self):
#         self.stream.close()
#         self.p.terminate()

# audio_stream = PyAudioSource(
#     device_index = 24,
#     sample_rate = 16000,
#     channels = 1,
#     frames_per_buffer = 2048,
#     format = 'int16'
# )

# while True:
#     audio_frame = audio_stream.get_audio_frame()
#     print(audio_frame)
#     print("Ho sentito qualcosa!")
