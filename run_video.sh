python -m src.main +experiment=VinAI checkpointing.load=checkpoints/re10k.ckpt mode=test dataset/view_sampler=evaluation dataset.view_sampler.index_path=assets/evaluation_index_VinAI_nctx2.json test.save_video=true test.save_image=false test.compute_scores=false