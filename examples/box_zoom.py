import mpld3
from mpld3.plugins import PluginBase


class BoxZoomPlugin(PluginBase):
    """Box Zoom"""

    JAVASCRIPT = r"""

    mpld3.BoxZoomPlugin = function(fig, prop){
	this.fig = fig;
	this.prop = mpld3.process_props(this, prop, {}, []);
        this.actions = ["drag"];

	// add a button to enable/disable box zoom
	mpld3.ButtonFactory({
	    toolbarKey: "boxzoom",
            sticky: true,
            actions: ["drag"],
	    onActivate: this.activate.bind(this),
	    onDeactivate: this.deactivate.bind(this),
            onDraw: this.deactivate.bind(this),
	    icon: function(){return mpld3.icons["zoom"];},
	});
	this.fig.prop.toolbar.push("boxzoom");
    };

    mpld3.BoxZoomPlugin.prototype.activate = function(){
         if(this.enable) this.enable();};
    mpld3.BoxZoomPlugin.prototype.deactivate = function(){
         if(this.disable) this.disable();};

    mpld3.BoxZoomPlugin.prototype.draw = function(){
	mpld3.insert_css("#" + this.fig.figid + " rect.extent",
			 {"fill": "#fff",
                          "fill-opacity": 0,
                          "stroke": "#999"});

	var brush = d3.svg.brush()
	    .x(this.fig.axes[0].x)
            .y(this.fig.axes[0].y)
            .on("brushend", brushend.bind(this));

	this.fig.root.selectAll(".mpld3-axes")
	    .data(this.fig.axes)
	    .call(brush)

	this.enable = function(){
            brush.on("brushstart", brushstart);
            this.fig.canvas.selectAll("rect.background")
		.style("cursor", "crosshair");
            this.fig.canvas.selectAll("rect.extent, rect.resize")
		.style("display", null);
            this.enabled = true;
	}
	
	this.disable = function(){
            brush.on("brushstart", null).clear();
            this.fig.canvas.selectAll("rect.background")
		.style("cursor", null);
            this.fig.canvas.selectAll("rect.extent, rect.resize")
		.style("display", "none");
            this.enabled = false;
	}

	this.toggle = function(){
	    this.enabled ? this.disable() : this.enable();
	}

	function brushstart(d, i){
	    brush.x(d.x).y(d.y);
	}

	function brushend(d, i){
	    if(this.enabled){
		var extent = brush.extent();
                if(extent[0][0] != extent[1][0] &&
                   extent[0][1] != extent[1][1]){
		    d.set_axlim([extent[0][0], extent[1][0]],
		        	[extent[0][1], extent[1][1]]);
                }
	    }
	    d.axes.call(brush.clear());
	}
    }

    mpld3.register_plugin("boxzoom", mpld3.BoxZoomPlugin);
    
    mpld3.icons['zoom'] = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBI\nWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3gMPDiIRPL/2oQAAANBJREFUOMvF0b9KgzEcheHHVnCT\nKoI4uXbtLXgB3oJDJxevw1VwkoJ/NjepQ2/BrZRCx0ILFURQKV2kyOeSQpAmn7WDB0Lg955zEhLy\n2scdXlBggits+4WOQqjAJ3qYR7NGLrwXGU9+sGbEtlIF18FwmuBngZ+nCt6CIacC3Rx8LSl4xzgF\nn0tusBn4UyVhuA/7ZYIv5g+pE3ail25hN/qdmzCfpsJVjKKCZesDBwtzrAqGOMQj6vhCDRsY4ALH\nmOVObltR/xeG/jph6OD2r+Fv5lZBWEhMx58AAAAASUVORK5CYII=\n"
    """

    def __init__(self):
        self.dict_ = {"type":"boxzoom"}


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    fig, ax = plt.subplots(2, 2, sharex='col', sharey='row')

    for i in range(2):
        for j in range(2):
            ax[i, j].plot(np.random.normal(0, 1, 100),
                          np.random.normal(0, 1, 100),
                          'ok', alpha=0.3)
    mpld3.plugins.connect(fig, BoxZoomPlugin())
    mpld3.show()
