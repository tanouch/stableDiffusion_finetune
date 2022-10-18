export MODEL_NAME="CompVis/stable-diffusion-v1-3"
export dataset_name="/home/u.tanielian/mytheresa_huggingface_datasets"

accelerate launch train_text_to_image.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --dataset_name=$dataset_name \
  --resolution=512 \
  --train_batch_size=2 \
  --gradient_accumulation_steps=1 \
  --gradient_checkpointing \
  --mixed_precision="fp16" \
  --max_train_steps=40000 \
  --learning_rate=5e-6 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --output_dir="mytheresa" 
