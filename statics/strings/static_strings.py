
# Directory Layout:

# Directory | base > data
_DIRECTORY_DATA = 'data'


# Directory | base > extractions
_DIRECTORY_EXTRACTIONS = 'data'

# Directory | base > extractions > models
_DIRECTORY_EXTRACTIONS_MODELS_ = 'models'

# Directory | base > extractions > models > _DIRECTORY_EXTRACTIONS__MODELS_KINEMATIC_SETS
_DIRECTORY_EXTRACTIONS__MODELS_KINEMATIC_SETS = 'kinematic_sets'

# argparse: static strings:
_ARGPARSE_DESCRIPTION = "Run DNN Replicas to extract the CFFs."

_ARGPARSE_ARGUMENT_INPUT_DATAFILE = '--input-datafile'
_ARGPARSE_ARGUMENT_KINEMATIC_SET_NUMBER = '--kinematic-set'
_ARGPARSE_ARGUMENT_NUMBER_REPLICAS = '--number-of-replicas'
_ARGPARSE_ARGUMENT_FORMALISM_VERSION = '--formalism'
_ARGPARSE_ARGUMENT_LEPTON_HELICITY = '--lepton-helicity'
_ARGPARSE_ARGUMENT_TARGET_POLARIZATION = '--target-polarization'
_ARGPARSE_ARGUMENT_VERBOSE = '--verbose'

_ARGPARSE_ARGUMENT_DESCRIPTION_INPUT_DATAFILE = 'Path to the input CSV file.'
_ARGPARSE_ARGUMENT_DESCRIPTION_KINEMATIC_SET_NUMBER = 'An integer specifying which kinematic set to analyze.'
_ARGPARSE_ARGUMENT_DESCRIPTION_NUMBER_REPLICAS = 'The number of DNN Replicas to run.'
_ARGPARSE_ARGUMENT_DESCRIPTION_FORMALISM_VERSION = 'The version of the formalism that we are using to analyze the cross section. Usually, it is BKM10.'
_ARGPARSE_ARGUMENT_DESCRIPTION_LEPTON_HELICITY = 'The incoming lepton helicitiy: positive or negative.'
_ARGPARSE_ARGUMENT_DESCRIPTION_TARGET_POLARIZATION = 'The nucleon target polarization: unpolarized or polarized.'
_ARGPARSE_ARGUMENT_DESCRIPTION_VERBOSE = 'Enable verbose logging.'

_COLUMN_NAME_KINEMATIC_SET = "set"

_COLUMN_NAME_X_BJORKEN = "x_b"
_COLUMN_NAME_Q_SQUARED = "QQ"
_COLUMN_NAME_T_MOMENTUM_CHANGE = "t"
_COLUMN_NAME_AZIMUTHAL_PHI = "phi_x"
_COLUMN_NAME_LEPTON_MOMENTUM = "k"

_COLUMN_NAME_CROSS_SECTION = "F"
_COLUMN_NAME_CROSS_SECTION_ERROR = "sigmaF"

# DNN Hyperparameters:
_HYPERPARAMETER_NUMBER_OF_EPOCHS = 1000
_HYPERPARAMETER_BATCH_SIZE = 16
_HYPERPARAMETER_LR_PATIENCE = 400
_HYPERPARAMETER_LR_FACTOR = 0.9
_HYPERPARAMETER_EARLYSTOP_PATIENCE_INTEGER = 1000

_DNN_VERBOSE_SETTING = 2