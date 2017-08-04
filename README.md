# ccker - cocalc jupyter kernel

## development

```
cd ~/ccker
# edit files under hal_cocalc/
# install ~/.local/share/jupyter/kernels/cocalc/kernel.json
python3 -m hal_cocalc.install --user
# run
jupyter console --kernel=cocalc

# install hal_cocalc module locally so it can be seen from other directories
pip3 install --user --upgrade .

# run mocha tests
cd ~/cocalc/src/smc-project/jupyter/test
which mocha
==> ~/cocalc/src/smc-hub/node_modules/.bin/mocha

mocha --opts test/mocha.opts test/dev-kernel.coffee
# or
DEBUG=1 mocha --opts test/mocha.opts test/dev-kernel.coffee
```
