# For train

python -u train.py \
  --train_data_path /workspace/data/knowledgegraph/webqsp_train.json \
  --dev_data_path /workspace/data/knowledgegraph/webqsp_dev.json \
  --model_size large \
  --per_gpu_batch_size 1 \
  --n_context 100 \
  --max_passage_length 200 \
  --total_step 100000 \
  --name FiD_wksp \
  --model_path  /workspace/data/pretrained/ \
  --checkpoint_dir /workspace/data/checkpoint/cache/  \
  --eval_freq 150 \
  --eval_print_freq 150



# For test


python test.py \
  --model_path /workspace/data/checkpoint/cache/best-dev/ \
  --test_data_path /workspace/data/knowledgegraph/webqsp_test.json \
  --model_size large \
  --per_gpu_batch_size 4 \
  --n_context 150 \
  --name FiD_wksp_test \
  --checkpoint_dir /workspace/data/checkpoint/snapshot \
  --write_test_results