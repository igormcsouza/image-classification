from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='imageclassification',
    version='1.0',
    packages=setuptools.find_packages(),    
    install_requires=[
        # 'numpy==1.18.0',
        'opencv-python==4.2.0.32',
        'imutils==0.5.3'
        # 'Keras==2.3.1'
    ],
    url='https://github.com/igormcsouza/image-classification',
    author='Igor Souza',
    author_email='igormcsouza@gmail.com',
    description='Image Classifiers and Preprocessors',
    long_description=long_description,
    long_description_content_type="text/markdown",
)