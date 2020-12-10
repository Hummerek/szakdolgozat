import subprocess
import pkg_resources
import sys

required = ['nltk', 'sklearn', 'gensim', 'matplotlib', 'pandas', 'keras', 'tensorflow', 'openpyxl']
installed = [pkg.key for pkg in pkg_resources.working_set]
for element in required:
  if element not in installed:
    print("[STA]: The following module is required, but not installed: " + element + ". Automatic installation will take place.")
    python = sys.executable
    if(element == 'nltk'):
      subprocess.check_call([python, '-m', 'pip', 'install', 'nltk'], stdout=subprocess.DEVNULL)
    if(element == 'sklearn'):
      subprocess.check_call([python, '-m', 'pip', 'install', 'scikit-learn==0.22.2'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'numpy'], stdout=subprocess.DEVNULL) #numpy version causes problems with windows
      subprocess.check_call([python, '-m', 'pip', 'install', 'numpy==1.19.3'], stdout=subprocess.DEVNULL)
    if(element == 'gensim'):
      subprocess.check_call([python, '-m', 'pip', 'install', 'gensim'], stdout=subprocess.DEVNULL)
    if(element == 'matplotlib'):
      subprocess.check_call([python, '-m', 'pip', 'install', 'matplotlib'], stdout=subprocess.DEVNULL)
    if(element == 'pandas'):
      subprocess.check_call([python, '-m', 'pip', 'install', 'pandas'], stdout=subprocess.DEVNULL)
    if(element == 'keras'):
      subprocess.check_call([python, '-m', 'pip', 'install', 'pyyaml'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'h5py'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'keras'], stdout=subprocess.DEVNULL)
    if(element == 'tensorflow'):
      subprocess.check_call([python, '-m', 'pip', 'install', 'absl_py==0.11.0'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'google_pasta==0.2.0'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'grpcio==1.33.2'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'h5py==2.10.0'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'Keras_Preprocessing==1.1.2'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'opt_einsum==3.3.0'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'protobuf==3.14.0'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'scipy==1.4.1'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'tensorboard==2.2.2'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'google_auth==1.23.0'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'Markdown==3.3.3'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'pyasn1==0.4.8'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'requests==2.25.0'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'certifi==2020.11.8'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'oauthlib==3.1.0'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'rsa==4.6'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'tensorboard_plugin_wit==1.7.0'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'tensorflow_estimator==2.2.0'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'urllib3==1.26.2'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'Werkzeug==1.0.1'], stdout=subprocess.DEVNULL)
      subprocess.check_call([python, '-m', 'pip', 'install', 'tensorflow==2.2'], stdout=subprocess.DEVNULL)
    if(element == 'openpyxl'):
      subprocess.check_call([python, '-m', 'pip', 'install', 'openpyxl'], stdout=subprocess.DEVNULL)

from Classihub import Classihub_class as chb

classihub_object = chb.Classihub_class()

