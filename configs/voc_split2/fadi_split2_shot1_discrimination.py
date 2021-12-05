_base_ = '../voc_split1/fadi_split1_shot1_discrimination.py'

split = 2
shot = 1

model = dict(roi_head=dict(
    bbox_head=dict(split=split, loss_margin=dict(shot=shot))))

data = dict(train=dict(split=split, shot=shot),
            val=dict(split=split),
            test=dict(split=split))

optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)

# learning policy
lr_config = dict(policy='step',
                 warmup='linear',
                 warmup_iters=1,
                 warmup_ratio=0.001,
                 step=[2500])

# Runner type
runner = dict(max_iters=3000)

checkpoint_config = dict(interval=500)
evaluation = dict(interval=500)

load_from = f'work_dirs/fadi_split{split}_shot{shot}_association/latest.pth'
