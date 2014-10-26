import matplotlib.pyplot as plt, mpld3

with open('_test_plots.html', 'w') as f:
    plt.plot([3,1,4,1,5,9,2], 'ks-', mew=3, mec='w', ms=10)
    mpld3.save_html(plt.gcf(), f, template_type='simple',
                    mpld3_url='mpld3/js/mpld3.v0.3git.js',
                    figid='mpld3_fig')
    f.write('\n\n\n<script type="text/javascript">\n')

    f.write('var f1=')
    mpld3.save_json(plt.gcf(), f)
    f.write(';\n\n')


    plt.plot([1,4,1,5,9,2,3], 'ks-', mew=3, mec='w', ms=10)
    f.write('var f2=')
    mpld3.save_json(plt.gcf(), f)
    f.write(';\n\n')

    f.write('</script>')

print("""

Ideally, it would then be possible to transition between
figures with javascript:
```
    mpld3.draw_figure("mpld3_fig", f2)
    mpld3.draw_figure("mpld3_fig", f1)
```
But that currently just adds an additional figure.

Making it work may require substantial refactoring of the js library.

""")
