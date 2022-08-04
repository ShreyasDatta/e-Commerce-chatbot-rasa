---
title: "**Rasa bot Knowledge Base docs**"
---

## Problem statement we tackle

Develop a chat-bot, capable of reading, deciphering context from user
messages, and output appropriate responses based on it.

## How we solved it utilizing ML capabilities?

We use Rasa Open Source. It is a ML framework for understanding
messages, holding conversations, regulating responses and custom user
queries, and connecting to messaging channels and APIs. The goal is to
train the bot, to identify phrases/words{entities} to predict the
'intent' of the user message. Based on this 'intent', appropriate
responses could be programmed.

#### How does it work

The recipes for a good ML-powered Bot includes: the Training Data; the
Response selector; the NLP pipeline.On that note, Rasa works on the
backbone of four important data files.

-   **Config.yml**\
    *The configuration file defines the components and policies that
    your model will use to make predictions based on user input. The
    Natural Language pre-processing that we perform on training data are
    abstracted here as configurable components. The language and
    pipeline keys specify the components used by the model to make NLU
    predictions. The policies key defines the policies used by the model
    to predict the next action.*

-   **Domain.yml** \#control operations for the bot from here\
    *The domain defines the universe in which your assistant operates.
    It specifies the intents, entities, slots, responses, forms, and
    actions your bot should know about. It also defines a configuration
    for conversation sessions.*

-   **Data/nlu.yml**\
    *NLU training data stores structured information about user
    messages. The goal of NLU (Natural Language Understanding) is to
    extract structured information from user messages. This usually
    includes the user\'s intent and any entities their message
    contains.*

-   **Data/stories.yml** \#example of intent/action sequences possible
    by the user\
    *Stories are a type of training data used to train your assistant\'s
    dialogue management model. Stories can be used to train models that
    are able to generalize to unseen conversation paths. It is a
    representation of a conversation between a user and an AI assistant,
    converted into a specific format where user inputs are expressed as
    intents (and entities when necessary), while the assistant\'s
    responses and actions are expressed as action names.*

#### Generating this NLU data

NLU (Natural Language Understanding) is the part of Rasa Open Source
that performs intent classification, entity extraction, and response
retrieval. NLU will take in a sentence such as \"I am looking for a
French restaurant in the center of town\" and return structured data
like:
```json
{
  "intent": "search_restaurant",
  "entities": {
    "cuisine": "French",
    "location": "center"
  }
}
```

And all of this is driven by a key principle called [Conversation-Driven
Development (CDD).]

#### **What is CDD?**

Conversation-Driven Development (CDD) is the process of listening to
your users and using those insights to improve your AI assistant. It is
the overarching best practice approach for chatbot development.

Developing great AI assistants is challenging because users will always
say something you didn\'t anticipate. The principle behind CDD is that
in every conversation users are telling you---in their own
words---exactly what they want. By practicing CDD at every stage of bot
development, you orient your assistant towards real user language and
behavior.

## The code base and project knowledge briefing

The project has three main working parts --

1.  The database where it fetches the data from,

2.  and the training data structuring the intents and stories for the
    bot.

3.  The action server and the custom actions .py file.

The NLU contains examples for intents and phrases to identify key
entities, which is then parsed, extracted and passed as a parameter for
the database query. This query fetches relevant data and the bot
structures that data and displays it as a meaningful response.

**Training Data - NLU**

If we look under the Data folder, there are a few .yml files. These
files contain all the example sentences/phrases/possible user messages,
that we use to train the bot. For ease of use, I have split these nlu
data into 2 categories:

**general-intents.yml**\
Contains examples of general, generic conversation starters, default
phrases, regularly occurring contexts. Some of them being: *Greet,
Goodbye, Affirmation, Denial, Postive-flow/happy-path,
Negative-flow/sad-path*

**Feature-intents.yml**\
Contains examples for specific use cases for the bot, invoking
functionality, asking questions, demanding requests or seeking help
through conversation contexts. Some of the example intents being:
*Discuss_purpose, Discuss_products, Figuring_out_user_product_choice,
Specific_product_query, Product_availability,
Additional_product_info_request*

**Stories.yml**\
Examples of conversation sequences with our feature-intents.
Constructing more diverse and varied story sequences accounting for more
obscure use-cases is a good practice for improving bot conversational
capabilities. Some story examples used for this;

-   story: explaining_bot_purpose

-   story: product_discussion

-   story: product_user_query

Another key feature of Rasa's story system, is the concept of 'rasa
interactive'. This CLI command enables us to train the bot real-time. It
starts an interactive learning session to create new training data by
chatting to your assistant. It allows us to input messages to the bot,
read how the NLU parser detects the message, predicts its possible
intent through a confidence rating and gives us the option to choose the
bot's next action/response to it, thus building an 'interactive-learning
story' for the bot to refer to.

#### The Database

With these training data, entity extraction components set up, the bot
is intended to refer/query attributes from a relational Database set up
using 'sqlite3'. The database 'chatb_db' was setup using python's
inbuilt 'sqlite3' module. We can work/interact with the database through
the terminal to make changes or import the sqlite3 module and run .py
files to make said changes.

The following is the Relational Schema for the DB:

![](https://i.imgur.com/Nj3MsPc.png)

>(note: As of now, only the __Product__ table and the __Order__
table has been setup)

The idea being, once the user requests for a particular item, or any
additional information related to it, the bot contextualizes it,
recognizes the entity (in the context, what product the user is
demanding) and communicates with the DB through custom py_actions
utlising the 'rasa_sdk' library.

#### Actions.py and the action server; the heart of the entire bot

What are actions? To put simply, after each user message, the model will
predict an action that the assistant should perform next. There are some
in-built actions that trigger by default or during fallbacks exceptions.
For example of some default actions,

-   after every new message, the start of a conversation, or after the
    conclusion of one set of actions, the bot executes
    *'action_listen',* which waits and listens for user input.

-   *'A response'* is a message the assistant will send back to the
    user. This is the action you will use most often, when you want the
    assistant to send text, images, buttons or similar to the user.

But for our purpose or specific user, we utlilise, a [custom
action] which is an action that can run any code you want. This can
be used to make an API call, or to query a database for example. They
can turn on the lights, add an event to a calendar, check a user\'s bank
balance, or anything else you can imagine.

The custom actions file used in this project is named 'actions.py' found
in /actions/actions.py. It contains the methods for all the query types,
what to do with that fetched data from the query, how to provide that
information to the bot through the tracker and how to query from
database.

In the following project, the scripts are divided into the following
main classes,

1.  collectProductInfo

> Essential driver class where methods from subsequent feature classes
> are invoked and bot responses and bot actions are handled through
> here. We collect information(like last_user_message,
> entities_extracted, latest_intent) from the [tracker]{*a class
> from rasa_sdk which keeps track of conversations and key information
> from the bot*} and pass it as arguments for the necessary methods we
> invoke and return a [bot_response].

2.  dbQueryMethods

> Contains definitions for different querying techniques. They are
> invoked by the collectProductInfo when needed, and the results are
> used accordingly.

```
def get_closest_value
```

-   Given a database column & text input, find the closest match for the
    input in the column.

-   We utilize fuzzy_matching here get a ratio for the similarity
    between user extracted role/category info and the database entry,
    and choose the one with the highest value.

```
def select_by_category
```
-   In the driver class, we first extract the closest_value from the
    (get_closest_value) method invoked earlier in the driver class, and
    with its result we pass it as argument for this method.

-   Here we use the value to query the database and search through the
    column/attribute ProductCategory and find the closest match.
```
def select_by_slots
```
-   Similar process as earlier, only here we query the ProductRole
    column to find the closest match.
```
def rows_as_info_text
```
-   Method which receives the query result from the cursor, manipulates
    it as a python list to check if its empty or not. It is and should
    be invoked at the end of every definition dealing with a query to
    receive that result and manipulate it accordingly.

3.  QueryOrderUpdate

> Class dealing with order update methods. Here every time an order is
> confirmed it is updated in the Order table.

4.  QueryOrderStatus

> Class checking the status of an order and passing the result as a
> response to the user.

### Project Organization


    ├── config.yml         <- all the ML settings, configurations and component selections
    │
    ├── actions
    │  └── actions.py     <- he core python script containing custom actions
    │
    ├── domain.yml        <- overview of all intents+responses+custom action
    │
    └── chatb_db
        ├── sqlTemp.db
        ├── sql-temp.py         <- The database for all our products and relevant schemas
        ├── productDataTable.csv
        └── db-connection.py    <- testing db connection cursor and query logic
    │
    └──  data
        │
        ├── feature-intents.yml  <- training data for different feature intents
        ├── rules.yml
        ├── nlu.yml            <- default/boiler-plate nlu data
        ├── stories.yml
        └── general-intents.yml <- training data for general-purpose intents   


### GLOSSARY

**Slots**

slots are your bot\'s memory. They act as a key-value store which can be
used to store information the user provided (e.g their home city) as
well as information gathered about the outside world (e.g. the result of
a database query).

**Entities**

Entities are structured pieces of information that can be extracted from
a user\'s message.

Entities are annotated in training examples with the entity\'s name. In
addition to the entity name, we can annotate an entity with synonyms,
roles, or groups.

**Tracker**

Rasa Open Source component that maintains the state of the dialogue,
which is represented as a JSON object listing the events from the
current session

**Config.yml**

The configuration file defines the components and policies that our
model will use to make predictions based on user input.

The language and pipeline keys specify the [components] used by the
model to make NLU predictions. The policies key defines the
[policies] used by the model to predict the next action.

**Training Pipeline and policies**

Components make up your NLU pipeline and work sequentially to process
user input into structured output. There are components for entity
extraction, for intent classification, response selection,
pre-processing, and more.

Some components that we are using:

-   Whitespace Tokenizer \#Tokenizer using whitespaces as a separator

-   CountVectorsFeaturizer \#Creates bag-of-words representation of user
    messages, intents, and responses

-   LexicalSyntacticFeaturizer \#Creates lexical and syntactic features
    for a user message to support entity extraction.

-   RegexFeaturizer \#Creates a vector representation of user message
    using regular expressions.

-   DIETClassifier \#Dual Intent Entity Transformer (DIET) used for
    intent classification and entity extraction

**Policies**

Techniques our bot uses to decided on how to respond back to user at
every step of the conversation. There are machine-learning and
rule-based policies that our assistant can use in tandem. We can
customize the policies our assistant uses by specifying the policies key
in our project\'s 'config.yml'.

Default policy priority

-   [Rule Policy]

> The RulePolicy is a policy that handles conversation parts that follow
> a fixed behavior (e.g. business logic). It makes predictions based on
> any rules you have in your training data.

-   [Memorization Policy]

> The MemoizationPolicy remembers the stories from your training data.
> It checks if the current conversation matches the stories in your
> stories.yml file. If so, it will predict the next action from the
> matching stories of your training data with a confidence of 1.0. If no
> matching conversation is found, the policy predicts None with
> confidence 0.0.

-   [TED Policy]

> The Transformer Embedding Dialogue (TED) Policy is a multi-task
> architecture for next action prediction and entity recognition.
