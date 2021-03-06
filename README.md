# py-meh
This is a simple wrapper for the [meh.com](https://meh.com) api.

## Installation
### From Source
```
$ pip install git+https://github.com:tizz98/py-meh.git@master
```

### PyPI
Coming soon.

## Get Started
```python
>>> import meh
>>> meh.api_key = 'xxx-your-key-here-xxx'
>>> meh.get_current()
```

### Response

The return value is a dict of the JSON response outlined below.

#### Deal

- **features**: The features of the deal in Markdown format.
- **id**: The unique identifier of the deal.
- **items**: An array of items for this deal. Items represent the individual products available for purchase and contain attributes (key/value pairs such as Color: Georgia Red), condition (New or Refurbished), the item’s unique identifier, the price, and a photo URL.
- **launches**: We break the meh.com daily deal into three launches as outlined here. The launches array provides data about the status of these launches.
- **photos**: An array of image URLs for the deal.
- **title**: The title of the deal.
- **soldOutAt**: If the deal has sold out, this field contains a timestamp of when the last item was purchased.
- **specifications**: The full product specs of the deal in Markdown format.
- **story**: The deal’s story, including the title and the body in Markdown format.
- **theme**: The theme for the deal including the accent color, background color, background image, and whether the foreground is light or dark.
- **topic**: Data about the forum topic for the deal including how many comments, replies, votes the topic has and the topic’s URL.
- **url**: The full permalink of the deal.

#### Poll

- **answers**: An array of possible answers to the poll. Each answer includes a unique identifier, the answer text, and the number of votes that answer has received.
- **id**: The unique identifier of the poll.
- **startDate**: The timestamp of when the poll started.
- **title**: The title of the poll.
- **topic**: Data about the forum topic for the poll including how many comments, replies, votes the topic has and the topic’s URL.

#### Video

- **id**: The unique identifier of the video.
- **startDate**: The timestamp of when the video started.
- **title**: The title of the video.
- **topic**: Data about the forum topic for the video including how many comments, replies, votes the topic has and the topic’s URL.
- **url**: The URL to the video.

### Example JSON
```json
{
  "deal": {
    "features": "- You get a pair of standard-size shredded memory foam pillows like everybody's talking about these days, to the extent that anyone talks about pillows at all\r\n- Bamboo rayon cover is hypoallergenic because bamboo secretes a substance called \"kun\" that kills microbes dead (seriously, it's true)\r\n- We laid our heads on these and found them plush and supportive, a little on the firm side and softening over time; your head may vary\r\n- Model: **BK1515** (nice little number, but it don't mean a thing if it ain't got that Google uniqueness - search results include a bar sink, an error code, a ball bearing, just about everything but these pillows)",
    "id": "a6k310000004DvGAAU",
    "items": [
      {
        "attributes": [
          
        ],
        "condition": "New",
        "id": "105563",
        "price": 20,
        "photo": "https:\/\/res.cloudinary.com\/mediocre\/image\/upload\/v1468876208\/huvffpdtsofwqgqt7ebq.png"
      }
    ],
    "launches": [
      {
        "soldOutAt": "2016-07-19T11:09:54.464Z"
      },
      {
        "soldOutAt": "2016-07-19T13:16:47.440Z"
      }
    ],
    "photos": [
      "https:\/\/res.cloudinary.com\/mediocre\/image\/upload\/v1468876208\/huvffpdtsofwqgqt7ebq.png",
      "https:\/\/res.cloudinary.com\/mediocre\/image\/upload\/v1468873794\/bgkb71dmccyk2puo0b9j.png",
      "https:\/\/res.cloudinary.com\/mediocre\/image\/upload\/v1468874174\/dfnqzdfnkdszv0qeizey.png",
      "https:\/\/res.cloudinary.com\/mediocre\/image\/upload\/v1468948067\/oaoezhraguwzngu7mjtk.gif"
    ],
    "title": "2-Pack: Bamboo Pillows",
    "specifications": "Specs \r\n====\r\n- Model: BK1515\r\n- Condition: New\r\n- Filling: 100% shredded polyurethane memory foam\r\n- Cover: Rayon made from bamboo\r\n- Hypoallergenic and antibacterial materials\r\n- Size: ~ 22\" x 13\" x 7\"\r\n\r\nWhat's in the Box? \r\n====\r\n2x Pillows\r\n\r\nPictures\r\n====\r\n[Packaging](https:\/\/res.cloudinary.com\/mediocre\/image\/upload\/v1468873794\/bgkb71dmccyk2puo0b9j.png)\r\n[Pillows](https:\/\/res.cloudinary.com\/mediocre\/image\/upload\/v1468874174\/dfnqzdfnkdszv0qeizey.png)\r\n[Pillow](https:\/\/res.cloudinary.com\/mediocre\/image\/upload\/v1468874174\/dfnqzdfnkdszv0qeizey.png)\r\n\r\nPrice Comparison\r\n====\r\n[$49.98 (for 2 similar) at Amazon](https:\/\/www.amazon.com\/dp\/B00OI3V5W2\/?tag=meh0ec-20)\r\n[$79.98 List](http:\/\/www.beautyko.com\/index.php?route=product\/product&product_id=972)\r\n*Find a relevant price comparison? Please share it in a comment in this thread :)*\r\n**Shipping:** $5 or free with **[VMP](http:\/\/bit.ly\/29PL2Wp)**",
    "story": {
      "title": "Sleep like you're paying for it.",
      "body": "It's a dark irony. You can't sleep at night because you're searching for a good night's sleep. You literally can't rest until you've tracked down those excellent pillows from your last hotel stay. Gentle yet firm. Soft yet supportive. You want those pillows. You *need* those pillows.\r\n\r\nThe tags on the pillows was no help about where to buy more: not so much as a web URL. The cleaning lady just rolled her eyes at you. After much irritable sighing, the front desk eventually tracked down a phone number for Jeff at the hotel procurement office. \r\n\r\nJeff's voicemail greeting said he'll be on vacation all summer, but you can call Rachel. You took a day off work to call Rachel, leaving increasingly desperate pleas for those pillows. Somehow you missed her one call back: that she really works better over email.\r\n\r\nShe still hasn't answered your email. You can't go on living this way. But you can't go on living without *those pillows*.\r\n\r\nIt doesn't have to be like this. There is a way out. These shredded memory foam pillows offer hotel-style comfort and a hypoallergenic bamboo rayon cover, all with a legitimate provenance. If you buy three pairs, you can be set for years to come, for less than the cost of a one-night stay in the crappiest motel. Not to mention the emotional cost of waiting for an email that never comes."
    },
    "theme": {
      "accentColor": "#87081b",
      "backgroundColor": "#a8d3bd",
      "backgroundImage": "https:\/\/res.cloudinary.com\/mediocre\/image\/upload\/v1468872225\/yxp0mrf5oz09hjksdnwz.jpg",
      "foreground": "dark"
    },
    "url": "https:\/\/meh.com\/deals\/2-pack--bamboo-pillows",
    "soldOutAt": "2016-07-19T20:01:05.611Z",
    "topic": {
      "commentCount": 58,
      "createdAt": "2016-07-19T04:00:05.126Z",
      "id": "578da5c5a91a0e1004716b33",
      "replyCount": 41,
      "url": "https:\/\/meh.com\/forum\/topics\/2-pack-bamboo-pillows",
      "voteCount": 2
    }
  },
  "poll": {
    "answers": [
      {
        "id": "a6l31000000CiVpAAK-1",
        "text": "I refuse to answer on the grounds that it may incriminate me",
        "voteCount": 207
      },
      {
        "id": "a6l31000000CiVpAAK-2",
        "text": "Yes, but it's been a long time",
        "voteCount": 133
      },
      {
        "id": "a6l31000000CiVpAAK-3",
        "text": "Only by accident! I swear!",
        "voteCount": 58
      },
      {
        "id": "a6l31000000CiVpAAK-4",
        "text": "Just, like, packets of coffee or the occasional Kleenex",
        "voteCount": 472
      },
      {
        "id": "a6l31000000CiVpAAK-5",
        "text": "No, but I've been tempted",
        "voteCount": 71
      },
      {
        "id": "a6l31000000CiVpAAK-6",
        "text": "Of course not. Who does that?",
        "voteCount": 220
      }
    ],
    "id": "a6l31000000CiVpAAK",
    "startDate": "2016-07-19T04:00:00.000Z",
    "title": "Have you ever walked off with anything from a hotel room? Towels, bedding, etc.?",
    "topic": {
      "commentCount": 22,
      "createdAt": "2016-07-19T03:59:59.218Z",
      "id": "578da5bfc8463928075e101a",
      "replyCount": 19,
      "url": "https:\/\/meh.com\/forum\/topics\/have-you-ever-walked-off-with-anything-from-a-hotel-room-towels-bedding-etc-",
      "voteCount": 3
    }
  },
  "video": {
    "id": "a6l31000000CiVpAAK",
    "startDate": "2016-07-19T04:00:00.000Z",
    "title": "When a Man Loves a Woman: Mad Ape Den Karaoke",
    "url": "https:\/\/www.youtube.com\/watch?v=k2AA7on_Kfw",
    "topic": {
      "commentCount": 7,
      "createdAt": "2016-07-18T04:00:03.483Z",
      "id": "578c5443a33960e40a91a670",
      "replyCount": 3,
      "url": "https:\/\/meh.com\/forum\/topics\/when-a-man-loves-a-woman-mad-ape-den-karaoke",
      "voteCount": 4
    }
  }
}
```
