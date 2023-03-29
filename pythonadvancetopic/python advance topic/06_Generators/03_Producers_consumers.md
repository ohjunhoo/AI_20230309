[Contents](../Contents.md) \| [Previous (6.2 Customizing Iteration)](02_Customizing_iteration.md) \| [Next (6.4 Generator Expressions)](04_More_generators.md)

# 6.3 Producers, Consumers and Pipelines

Generators are a useful tool for setting various kinds of
producer/consumer problems and dataflow pipelines.  This section
discusses that.

### Producer-Consumer Problems

Generators are closely related to various forms of *producer-consumer* problems.

```python
# Producer
def follow(f):
    ...
    while True:
        ...
        yield line        # Produces value in `line` below
        ...

# Consumer
for line in follow(f):    # Consumes value from `yield` above
    ...
```

`yield` produces values that `for` consumes.

### Generator Pipelines

You can use this aspect of generators to set up processing pipelines (like Unix pipes).

*producer* &rarr; *processing* &rarr; *processing* &rarr; *consumer*

Processing pipes have an initial data producer, some set of intermediate processing stages and a final consumer.

**producer** &rarr; *processing* &rarr; *processing* &rarr; *consumer*

```python
def producer():
    ...
    yield item
    ...
```

The producer is typically a generator. Although it could also be a list of some other sequence.
`yield` feeds data into the pipeline.

*producer* &rarr; *processing* &rarr; *processing* &rarr; **consumer**

```python
def consumer(s):
    for item in s:
        ...
```

Consumer is a for-loop. It gets items and does something with them.

*producer* &rarr; **processing** &rarr; **processing** &rarr; *consumer*

```python
def processing(s):
    for item in s:
        ...
        yield newitem
        ...
```

Intermediate processing stages simultaneously consume and produce items.
They might modify the data stream.
They can also filter (discarding items).

*producer* &rarr; *processing* &rarr; *processing* &rarr; *consumer*

```python
def producer():
    ...
    yield item          # yields the item that is received by the `processing`
    ...

def processing(s):
    for item in s:      # Comes from the `producer`
        ...
        yield newitem   # yields a new item
        ...

def consumer(s):
    for item in s:      # Comes from the `processing`
        ...
```

Code to setup the pipeline

```python
a = producer()
b = processing(a)
c = consumer(b)
```

You will notice that data incrementally flows through the different functions.
