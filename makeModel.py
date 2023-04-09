import logging 
from simpletransformers.question_answering import QuestionAnsweringModel, QuestionAnsweringArgs


logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)


model_args = QuestionAnsweringArgs()
model_args.train_batch_size = 1


# BERT 모델 다운로드
model = QuestionAnsweringModel(
    "bert", "bert-base-multilingual-cased", args=model_args,
    
    # GPU 없이 돌릴 때
    use_cuda=False
)