import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=str, default="8097")
parser.add_argument("--train", action='store_true')
parser.add_argument("--object", default='car', help='Object specific GAN training')
parser.add_argument("--predict", action='store_true')
parser.add_argument("--name",  type=str, default="enlightening")

opt = parser.parse_args()

if opt.train:
	os.system("python train.py \
		--dataroot /work/zk315372/Pai/EnlightenGAN_Data \
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
		--batchSize 4 \
        --self_attention \
		--use_norm 1 \
		--use_wgan 0 \
        --use_ragan \
        --hybrid_loss \
        --times_residual \
		--instance_norm 0 \
		--vgg 1 \
        --vgg_choose stylefeat \
		--gpu_ids 1 \
		--resize_or_crop resize_and_crop \
		--object {} \
		--display_port={}".format(opt.object, opt.port))

elif opt.predict:
	for i in range(1, 2):
	        os.system("python predict.py \
				--object {} \
	        	--dataroot /work/vq218944/MSAI/EnlightenGAN_Data/\
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
	        	--instance_norm 0 --resize_or_crop='no'\
	        	--which_epoch {}".format(opt.object, opt.name, str(200 - i*5)))
