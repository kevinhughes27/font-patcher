font-patcher
============

I recently came across a screenshot on [r/vimporn](https://www.reddit.com/r/vimporn/comments/uf4mgy/neovim_tmux/) that I fell in love with. The separators in particular were so slick I had to have them.

However after looking at the code and finding the symbol they used I could not get the same effect. In fact it looked terrible on my system!

![alacritty](./imgs/alacritty.png)

I asked the OP and they told me the screenshot was taken using [kitty](https://sw.kovidgoyal.net/kitty/) and not [alacritty](https://alacritty.org/) despite having both configured in their dotfiles.

I tried kitty and the symbol rendered nicely the way I wanted it:

![kitty](./imgs/kitty.png)

This can be minimally reproduced with the following in a shell:

`echo -e "\ue0b8"`

Now the question is why?

After some digging I figured out this is because kitty (and some other terminals) don't use the user's font for rendering certain characters and use their own custom internal font instead (https://github.com/alacritty/alacritty/issues/5485). I'm no terminal expert but I tend to agree with alacritty that a terminal shouldn't do this, however I also really like the way kitty renders this character.

Which brings me to this project - can I fix it by fixing the font? YES!

I looked into how the [nerd-fonts](https://github.com/ryanoasis/nerd-fonts/blob/master/font-patcher) font patcher works and learned it uses [fontforge](https://fontforge.org/en-US/) and the fontforge python bindings. After a bit of trial and error I came up with my own little script to patch the separators I cared about to render like they do in kitty.

 Now I'm free to use whichever terminal I feel like and I learned something about terminals and fonts!
