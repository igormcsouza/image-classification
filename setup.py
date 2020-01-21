from setuptools import setup

setup(
    name='image_classification',
    version='1.0',
    package_dir={'': 'image_classification'},
    install_requires=[
        'numpy==1.18.0',
        'opencv-python==4.1.2.30',
        'Keras==2.3.1'
    ],
    url='https://github.com/igormcsouza/image-classification',
    author='Igor Souza',
    author_email='igormcsouza@gmail.com',
    description='Image Classifiers and Preprocessors'
)