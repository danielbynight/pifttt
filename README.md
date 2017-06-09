# PIFTTT

It stands for "**P**ython **IFTTT**".
A simple package to facilitate sending requests to IFTTT's
"Maker Webhooks".

## Quick start

The one method you're looking for is `pifttt.if_this`. To use it,
pass in your key and the name of the event you want to trigger, as
well as any optional values (up to three). For example:
```Python
if_this(
    key='super-secret',
    event_name='name of event,
    value1='So',
    value2='long',
    value3='and thanks for all the fish',
)
```

## Return values and exceptions

In case of a successful response from IFTTT (i.e., a status code of 200),
the content of the response will be returned. Otherwise, an exception
will be raised. IFTTT is not very strict, therefore there is not
much where to go wrong (for example, triggering a non-existent event
or not send a value expected by an event will both be allowed).

These are the exceptions the package raises:

### `HookRequestError(Exception)`

A blanket exception raised when something went wrong with the request,
but not much information about the error was found. The response from
IFTTT can be found in its `response` property.

### `InvalidKey(HookRequestError)`

The key sent was not recognized by IFTTT.

### `InvalidArgument(Exception)`

One of the arguments passed to `if_this` is wrong (probably contains an
illegal character).


## Customization

If you'd like to go a little bit further, you could use the class
`IFTTTWebhook(key, event_name)` to customize your requests.
Requests are sent from this class with the method
 `send(value1=None, value2=None, value3=None`.
