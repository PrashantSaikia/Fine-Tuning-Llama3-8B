# FIne-Tuning-Llama-3-8B

### SSH to the EC2 instance:
`ssh -i "prasanta_key.pem" ubuntu@54.72.144.211`

### Copy the files from local to EC2 instance
```
scp -i prasanta_key.pem -r /Users/Admin/Documents/Uncensored\ LLM/Charlie-Uncensored-LLM-Chatbot/FineTuningDatasetGeneration/FineTuningDataset.csv ubuntu@54.72.144.211:/home/ubuntu/FineTuning

scp -i prasanta_key.pem -r /Users/Admin/Documents/Uncensored\ LLM/Charlie-Uncensored-LLM-Chatbot/FineTuningDatasetGeneration/fine_tuning.py ubuntu@54.72.144.211:/home/ubuntu/FineTuning
```
### Output
```
🦥 Unsloth: Will patch your computer to enable 2x faster free finetuning.
==((====))==  Unsloth 2024.8: Fast Llama patching. Transformers = 4.44.1.
   \\   /|    GPU: NVIDIA A10G. Max memory: 21.988 GB. Platform = Linux.
O^O/ \_/ \    Pytorch: 2.3.1+cu121. CUDA = 8.6. CUDA Toolkit = 12.1.
\        /    Bfloat16 = TRUE. FA [Xformers = 0.0.27. FA2 = False]
 "-____-"     Free Apache license: http://github.com/unslothai/unsloth
Unsloth 2024.8 patched 32 layers with 32 QKV layers, 32 O layers and 32 MLP layers.
Map: 100%|███████████████████████████████████████████| 76/76 [00:00<00:00, 16486.53 examples/s]
Map: 100%|████████████████████████████████████████████| 20/20 [00:00<00:00, 7017.41 examples/s]
Map (num_proc=2): 100%|█████████████████████████████████| 76/76 [00:00<00:00, 96.78 examples/s]
max_steps is given, it will override any value given in num_train_epochs
==((====))==  Unsloth - 2x faster free finetuning | Num GPUs = 1
   \\   /|    Num examples = 76 | Num Epochs = 7
O^O/ \_/ \    Batch size per device = 2 | Gradient Accumulation steps = 4
\        /    Total batch size = 8 | Total steps = 60
 "-____-"     Number of trainable parameters = 41,943,040
{'loss': 2.0337, 'grad_norm': 0.21303388476371765, 'learning_rate': 4e-05, 'epoch': 0.11}      
{'loss': 2.3725, 'grad_norm': 0.2101127803325653, 'learning_rate': 8e-05, 'epoch': 0.21}       
{'loss': 2.0626, 'grad_norm': 0.2363099902868271, 'learning_rate': 0.00012, 'epoch': 0.32}     
{'loss': 2.3268, 'grad_norm': 0.183258518576622, 'learning_rate': 0.00016, 'epoch': 0.42}      
{'loss': 2.0609, 'grad_norm': 0.24626605212688446, 'learning_rate': 0.0002, 'epoch': 0.53}     
{'loss': 1.8913, 'grad_norm': 0.28193438053131104, 'learning_rate': 0.00019636363636363636, 'epoch': 0.63}
{'loss': 2.3758, 'grad_norm': 0.7412992119789124, 'learning_rate': 0.00019272727272727274, 'epoch': 0.74}
{'loss': 1.9624, 'grad_norm': 0.3750440776348114, 'learning_rate': 0.0001890909090909091, 'epoch': 0.84}
{'loss': 1.8901, 'grad_norm': 0.32056891918182373, 'learning_rate': 0.00018545454545454545, 'epoch': 0.95}
{'loss': 1.9973, 'grad_norm': 0.2998574674129486, 'learning_rate': 0.00018181818181818183, 'epoch': 1.05}
{'loss': 2.3946, 'grad_norm': 0.27629178762435913, 'learning_rate': 0.0001781818181818182, 'epoch': 1.16}
{'loss': 1.8277, 'grad_norm': 0.3626636564731598, 'learning_rate': 0.00017454545454545454, 'epoch': 1.26}
{'loss': 1.8202, 'grad_norm': 0.26188164949417114, 'learning_rate': 0.0001709090909090909, 'epoch': 1.37}
{'loss': 1.9106, 'grad_norm': 0.2641196846961975, 'learning_rate': 0.00016727272727272728, 'epoch': 1.47}
{'loss': 1.8985, 'grad_norm': 0.4085584282875061, 'learning_rate': 0.00016363636363636366, 'epoch': 1.58}
{'loss': 1.7496, 'grad_norm': 0.3152574598789215, 'learning_rate': 0.00016, 'epoch': 1.68}     
{'loss': 1.6548, 'grad_norm': 0.3618781268596649, 'learning_rate': 0.00015636363636363637, 'epoch': 1.79}
{'loss': 1.6309, 'grad_norm': 0.3520793318748474, 'learning_rate': 0.00015272727272727275, 'epoch': 1.89}
{'loss': 2.0404, 'grad_norm': 0.2682135999202728, 'learning_rate': 0.0001490909090909091, 'epoch': 2.0}
{'loss': 2.0017, 'grad_norm': 0.2914141118526459, 'learning_rate': 0.00014545454545454546, 'epoch': 2.11}
{'loss': 1.404, 'grad_norm': 0.4504246115684509, 'learning_rate': 0.00014181818181818184, 'epoch': 2.21}
{'loss': 1.5507, 'grad_norm': 0.3516865074634552, 'learning_rate': 0.0001381818181818182, 'epoch': 2.32}
{'loss': 1.7239, 'grad_norm': 0.2866009771823883, 'learning_rate': 0.00013454545454545455, 'epoch': 2.42}
{'loss': 1.6878, 'grad_norm': 0.459661066532135, 'learning_rate': 0.00013090909090909093, 'epoch': 2.53}
{'loss': 1.8609, 'grad_norm': 0.36637774109840393, 'learning_rate': 0.00012727272727272728, 'epoch': 2.63}
{'loss': 1.4266, 'grad_norm': 0.4723108112812042, 'learning_rate': 0.00012363636363636364, 'epoch': 2.74}
{'loss': 1.9139, 'grad_norm': 0.36898818612098694, 'learning_rate': 0.00012, 'epoch': 2.84}    
{'loss': 1.6515, 'grad_norm': 0.5911470651626587, 'learning_rate': 0.00011636363636363636, 'epoch': 2.95}
{'loss': 1.5482, 'grad_norm': 0.4334719777107239, 'learning_rate': 0.00011272727272727272, 'epoch': 3.05}
{'loss': 1.428, 'grad_norm': 0.589687705039978, 'learning_rate': 0.00010909090909090909, 'epoch': 3.16}
{'loss': 1.6548, 'grad_norm': 0.44513940811157227, 'learning_rate': 0.00010545454545454545, 'epoch': 3.26}
{'loss': 1.4049, 'grad_norm': 0.6725494265556335, 'learning_rate': 0.00010181818181818181, 'epoch': 3.37}
{'loss': 1.5367, 'grad_norm': 0.5140148997306824, 'learning_rate': 9.818181818181818e-05, 'epoch': 3.47}
{'loss': 1.6043, 'grad_norm': 0.5121866464614868, 'learning_rate': 9.454545454545455e-05, 'epoch': 3.58}
{'loss': 1.309, 'grad_norm': 0.654462993144989, 'learning_rate': 9.090909090909092e-05, 'epoch': 3.68}
{'loss': 1.6608, 'grad_norm': 0.5241869688034058, 'learning_rate': 8.727272727272727e-05, 'epoch': 3.79}
{'loss': 1.7581, 'grad_norm': 0.43246403336524963, 'learning_rate': 8.363636363636364e-05, 'epoch': 3.89}
{'loss': 1.178, 'grad_norm': 0.8759654760360718, 'learning_rate': 8e-05, 'epoch': 4.0}         
{'loss': 1.527, 'grad_norm': 0.7515935897827148, 'learning_rate': 7.636363636363637e-05, 'epoch': 4.11}
{'loss': 1.0917, 'grad_norm': 0.6931533813476562, 'learning_rate': 7.272727272727273e-05, 'epoch': 4.21}
{'loss': 1.231, 'grad_norm': 0.6294010281562805, 'learning_rate': 6.90909090909091e-05, 'epoch': 4.32}
{'loss': 1.1209, 'grad_norm': 1.5152565240859985, 'learning_rate': 6.545454545454546e-05, 'epoch': 4.42}
{'loss': 1.5087, 'grad_norm': 0.7701089978218079, 'learning_rate': 6.181818181818182e-05, 'epoch': 4.53}
{'loss': 1.1792, 'grad_norm': 0.7641201615333557, 'learning_rate': 5.818181818181818e-05, 'epoch': 4.63}
{'loss': 1.3454, 'grad_norm': 0.6867017149925232, 'learning_rate': 5.4545454545454546e-05, 'epoch': 4.74}
{'loss': 1.3326, 'grad_norm': 0.6566607356071472, 'learning_rate': 5.090909090909091e-05, 'epoch': 4.84}
{'loss': 1.5379, 'grad_norm': 0.8035358786582947, 'learning_rate': 4.7272727272727275e-05, 'epoch': 4.95}
{'loss': 1.0965, 'grad_norm': 0.8311971426010132, 'learning_rate': 4.3636363636363636e-05, 'epoch': 5.05}
{'loss': 1.2337, 'grad_norm': 0.6756340265274048, 'learning_rate': 4e-05, 'epoch': 5.16}       
{'loss': 1.6962, 'grad_norm': 0.513672947883606, 'learning_rate': 3.6363636363636364e-05, 'epoch': 5.26}
{'loss': 1.2547, 'grad_norm': 0.7130318284034729, 'learning_rate': 3.272727272727273e-05, 'epoch': 5.37}
{'loss': 0.9514, 'grad_norm': 0.7440412044525146, 'learning_rate': 2.909090909090909e-05, 'epoch': 5.47}
{'loss': 0.7591, 'grad_norm': 0.8573436141014099, 'learning_rate': 2.5454545454545454e-05, 'epoch': 5.58}
{'loss': 1.4952, 'grad_norm': 1.0400276184082031, 'learning_rate': 2.1818181818181818e-05, 'epoch': 5.68}
{'loss': 1.6901, 'grad_norm': 0.8196322321891785, 'learning_rate': 1.8181818181818182e-05, 'epoch': 5.79}
{'loss': 1.3388, 'grad_norm': 0.927932858467102, 'learning_rate': 1.4545454545454545e-05, 'epoch': 5.89}
{'loss': 1.0573, 'grad_norm': 2.2638583183288574, 'learning_rate': 1.0909090909090909e-05, 'epoch': 6.0}
{'loss': 1.2928, 'grad_norm': 0.7036101818084717, 'learning_rate': 7.272727272727272e-06, 'epoch': 6.11}
{'loss': 1.1641, 'grad_norm': 0.6802316308021545, 'learning_rate': 3.636363636363636e-06, 'epoch': 6.21}
{'loss': 1.5269, 'grad_norm': 1.098676085472107, 'learning_rate': 0.0, 'epoch': 6.32}          
{'train_runtime': 635.8227, 'train_samples_per_second': 0.755, 'train_steps_per_second': 0.094, 'train_loss': 1.610592911640803, 'epoch': 6.32}
100%|██████████████████████████████████████████████████████████| 60/60 [10:35<00:00, 10.60s/it]
635.8227 seconds used for training.
10.6 minutes used for training.
Peak reserved memory = 9.359 GB.
Peak reserved memory for training = 3.531 GB.
Peak reserved memory % of max memory = 42.564 %.
Peak reserved memory for training % of max memory = 16.059 %.
```
