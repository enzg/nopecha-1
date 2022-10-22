Nopecha.com for Python
=

Supports Asynchronous functions

[Nopecha.com](https://Nopecha.com) package for Python3


#### Hcaptcha
```python
import nopecha

key = "YOUR KEY HERE"

def main():
    client = nopecha.New(key)
    balance = client.get_balance()
    image_urls = [f"https://www.nopecha.com/image/demo/hcaptcha/{i}.png" for i in range(9)]
    data = client.hcaptcha(image_urls, "Please click each image containing a cat-shaped cookie.")
    print(f"Balance: {balance}")
    print(f"Data: {data}")
    

if __name__ == "__main__":
    main()
```


#### ReCaptcha v2 and v3

```python
import nopecha

key = "YOUR KEY HERE"

def main():
    client = nopecha.New(key)
    balance = client.get_balance()
    image_urls = [f"https://www.nopecha.com/image/demo/recaptcha/{i}.png" for i in range(9)]
    data = client.recaptcha(image_urls, "Please click each image containing a palm tree.")
    print(f"Balance: {balance}")
    print(f"Data: {data}")
    
if __name__ == "__main__":
    main()
```


