from Preprocessor import Preprocessor_class as pre
from Encoder import Encoder_class as enc
import sys

preprocessor_object = pre.Preprocessor_class(sys.argv[1], sys.argv[2])
preprocessor_object.__process__()
preprocessed_results = preprocessor_object.__get_preprocessed_data__()

encoder_object = enc.Encoder_class(sys.argv[1], preprocessed_results)
encoder_object.__process__()