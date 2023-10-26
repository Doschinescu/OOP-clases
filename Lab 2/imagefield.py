from basefile import BaseFile

class ImageFile(BaseFile):
    def info(self):
        super().info()
        # We just simulate the real size of an image
        print(f"Image Size: 1024x860")