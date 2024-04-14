_base_ = [
    '../../_base_/default_runtime.py',
    '../../_base_/models/deeplabv3plus_r50-d8.py',
    '../../_base_/datasets/uda_gta_to_cityscapes_512x512.py',
    '../../_base_/uda/dacs.py',
    '../../_base_/schedules/adamw.py',
    '../../_base_/schedules/poly10warm.py'
]

n_gpus = 1
seed = 0
model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                      checkpoint='open-mmlab://resnet101_v1c')
    ),
    decode_head=dict(
        norm_cfg=None
    )
)
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=4,
    train=dict())

optimizer_config = None
optimizer = dict(
    lr=6e-05,
    paramwise_cfg=dict(
        custom_keys=dict(
            head=dict(lr_mult=10.0))))

runner = dict(
    type='IterBasedRunner',
    max_iters=40000)

checkpoint_config = dict(
    by_epoch=False,
    interval=20000,
    max_keep_ckpts=1)

evaluation = dict(interval=4000, metric='mIoU')

name = 'gta2cs_dacs_dlv3p_nodbn_r101v1c_poly10warm_s0'
exp = 1
name_dataset = 'gta2cityscapes'
name_architecture = 'dlv3p_nodbn_r101v1c'
name_encoder = 'r101v1c'
name_decoder = 'dlv3p_nodbn'
name_uda = 'dacs'
name_opt = 'adamw_6e-05_pmTrue_poly10warm_1x2_40k'
