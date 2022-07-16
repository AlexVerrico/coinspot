## Authentication
To use parts of this library, you may need an API Token. You can obtain one by following the official Coinspot instructions at the top of [this page](https://www.coinspot.com.au/v2/api)

## Nonce
The Coinspot documentation states that the nonce can be 
> Any integer value which must always be greater than the previous requests nonce value.

The default nonce used by this library is the output of 
```python
int(time() * 1000) 
```
which should be fine for most use cases, however any function that requires a nonce does allow you to provide one manually using the `nonce` kwarg.

## Next steps
[Public API (No API Key required)](public_api.md)  
[Read Only API](read_only_api.md)  
[Full Access API](full_access_api.md)  
