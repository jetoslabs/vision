What is real-time processing
    Processing frames on the fly without delay or loss

Basic criteria for real-time image processing:
    Process time per frame < Capture time per frame

Opinions on approach
    1. Try to process byte-array coming from the sensor, instead of decompressing in jpeg or other format
    2. Try to keep frame resolution as small as possible because image processing is basically matrix manipulation
    3. Try to use greyscale images instead of RGB images. Single channel image is easier to process than 3 channel image
    4. If the execution time is varying across frame, try to push new frames to bucket following FIFO and process frame from there