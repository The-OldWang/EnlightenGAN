import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=str, default="8097")
parser.add_argument("--train", action='store_true')
parser.add_argument("--object", default='car', help='Object specific GAN training')
parser.add_argument("--predict", action='store_true')
parser.add_argument("--name",  type=str, default="enlightening")
parser.add_argument("--suffix",  type=str, default="test_dataset1")
parser.add_argument("--gpu_ids",  type=str, default="0,1")
parser.add_argument("--data_path",  type=str, default="/home/vq218944/Downloads/EnlightenGAN_Data")

opt = parser.parse_args()

if opt.train:
	os.system("python train.py \
		--dataroot {} \
		--no_dropout \
		--name enlightening \
		--model single \
		--dataset_mode unaligned \
		--which_model_netG sid_unet_resize \
        --which_model_netD no_norm_4 \
        --patchD \
        --patch_vgg \
        --patchD_3 5 \
        --n_layers_D 5 \
        --n_layers_patchD 4 \
		--fineSize 256 \
        --patchSize 32 \
		--skip 1 \
		--batchSize 32 \
        --self_attention \
		--use_norm 1 \
		--use_wgan 0 \
        --use_ragan \
        --hybrid_loss \
        --times_residual \
		--instance_norm 0 \
		--vgg 1 \
        --vgg_choose stylefeat \
		--gpu_ids 0,1 \
		--resize_or_crop resize_and_crop \
		--object {} \
		--display_port={}".format(opt.data_path, opt.object, opt.port))

elif opt.predict:
	for i in range(1, 2):
	        os.system("python predict.py \
	        	--dataroot {} \
	        	--name {} \
	        	--model single \
	        	--which_direction AtoB \
	        	--no_dropout \
	        	--dataset_mode unaligned \
	        	--which_model_netG sid_unet_resize \
	        	--skip 1 \
	        	--use_norm 1 \
	        	--use_wgan 0 \
                --self_attention \
                --times_residual \
				--gpu_ids {} \
	        	--instance_norm 0 --resize_or_crop='no'\
	        	--which_epoch latest".format(opt.data_path, opt.name, opt.gpu_ids))
