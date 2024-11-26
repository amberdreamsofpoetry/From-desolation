If you tell ChatGPT to act like a cat, it will do so. You could instead train a model to only act like a cat. You could, in principle, train a model to do any simple task. I will argue for the use of a network of micro language models, each trained to do a specific task on a narrow input set, as an augmentation to the current large language models.

In my conception, models would be as small as echoing a single phrase up to the capacity of evaluating a specific function over any given input -- for example, determining the tone of a piece of text or returning the plural form of singular nouns. (Indeed, the former of these would not be much of a language model at all and would best be just a bit of code.) These models would be strung together into components and then further into networks employing larger-scale models in order to create efficient high-level functioning. This is analogous to building circuits out of logic gates instead of raw capacitors.

Tasks which are difficult to break down can be left to more complex models with minimal loss. However, those tasks which can be broken down will be, and the main large model or models will be relieved of the duty and are more freely able to spend their resources.

These micro models would be extremely cheap to train and deploy and would only be run when their specific output types are needed. This allows them to be used at scale and lets them function very modularly.

Determining whether a task is decomposable is exactly the sort of high-level task that we would leave to a large model until we figure out how to break it down. They currently function well as generalist solvers and our largest and most advanced models will serve well for ensuring safety in any human output, for example. The process of breaking down those sorts of problems is itself a problem which these networks could be employed to solve. We reap the benefit, however, by allowing ourselves to reuse components once they are already created.

Real-time conversation will indeed be hit, but this sort of network can be run and produce results with extremely minimal human intervention; if you give them a space to think and do not burden them with coming up with the right answer immediately, work can be done in the background.

#todo [Last message has some good next steps](https://chatgpt.com/c/67413ce4-51d8-8004-9bdb-79353226fbe1)
