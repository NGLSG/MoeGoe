from setuptools import setup, find_packages

setup(
    name='MoeGoe',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'numba',
        'librosa',
        'numpy==1.23',
        'flask_cors',
        'flask',
        'jsonify',
        'scipy',
        'torch',
        'unidecode',
        'openjtalk>=0.3.0.dev2',
        'jamo',
        'pypinyin',
        'jieba',
        'protobuf',
        'cn2an',
        'inflect',
        'eng_to_ipa',
        'ko_pron',
        'indic_transliteration',
        'num_thai',
        'opencc',
        'audonnx',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'moegoe = MoeGoe.__main__:main'
        ]
    },
    include_package_data=True,
    package_data={
        'MoeGoe': ['*.yaml']
    }
)