<div align="justify">

We need to define an API for our media platform, which allows us to display contents
following a hierarchical structure.
A Content can contain files (such as videos, pdfs, or text), a set of arbitrary metadata
associated with the content (content descriptions, authors, genre, etc.) and a rating
value which is a decimal number between 0 and 10.
See the following example of a Content, corresponding to an episode of a TV series.

<p align="center">
    <img src="/Images/InfoRagnar.png">
</p>



We organize the contents in the platform through the use of Channels. A Channel
stores the hierarchical structure and has a title, a language, and a picture. A channel
can contain references to either other channels or contents. If a channel has
subchannels, it cannot have any content underneath, conversely, if a channel has
contents, it cannot have any subchannel underneath. A channel must have at least
one content or one subchannel.

In the following images, you can see an example of the channels that could be provided
by your API.

<p align="center">
    <img src="/Images/Example.png">
</p>

The rating of a channel is the average of the ratings of all the channels underneath, if
the channel has no subchannels its rating is the average of the ratings of its contents. If
a channel has no contents, it does not affect the ratings of its parent since its value is
undefined.
Channels can’t store this rating directly (because the structure can change at any time), so we need a way to compute it from the content structure behind them.

</div>