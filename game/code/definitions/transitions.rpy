init -3 python:
    dissolve_scene = Fade(1.0, 1.0, 1.0)
    quick_fade = Fade(0.3, 0.05, 0.3)

    def NonBlockingTransition(trans):
        return {
            layer: trans 
            for layer in ("master", "above_master")
        }

    def NonBlockingDissolve(*args, **kwargs):
        return NonBlockingTransition(Dissolve(*args, **kwargs))