_base_ = 'fadi_split2_shot1_discrimination.py'

split = 2
shot = 3

model = dict(roi_head=dict(
    bbox_head=dict(split=split, loss_margin=dict(shot=shot))))

data = dict(train=dict(
    split=split,
    shot=shot,
))

# learning policy
lr_config = dict(policy='step',
                 warmup='linear',
                 warmup_iters=1,
                 warmup_ratio=0.001,
                 step=[10000])

# Runner type
runner = dict(max_iters=12000)

checkpoint_config = dict(interval=1000)
evaluation = dict(interval=1000)

load_from = f'work_dirs/fadi_split{split}_shot{shot}_association/latest.pth'
