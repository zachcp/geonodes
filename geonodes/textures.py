#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : textures
-----------------
- Create the textures

This module implementes texture creation as class meythod of Texture class.
Texture class inherits from TextureRoot which can be created as a Group Input.

```  python
# Create a noise texture
noise_node = Texture.Noise()
```

classes
-------
- Texture       : Implements the texture nodes creation
    - Brick
    - Checker
    - Gradient
    - Image
    - Magic
    - Noise
    - Voronoi
    - Wave
    - WhiteNoise

functions
---------

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
"""

from .treeclass import Node
from .socketclass import TextureRoot

class Texture(TextureRoot):

    @staticmethod
    def Brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None,
        bias=None, brick_width=None, row_height=None):
        """ Node 'Brick Texture' (ShaderNodeTexBrick)

        [!Node] Brick Texture

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - color1 (Color) : socket 'Color1' (Color1)
        - color2 (Color) : socket 'Color2' (Color2)
        - mortar (Color) : socket 'Mortar' (Mortar)
        - scale (Float) : socket 'Scale' (Scale)
        - mortar_size (Float) : socket 'Mortar Size' (Mortar Size)
        - mortar_smooth (Float) : socket 'Mortar Smooth' (Mortar Smooth)
        - bias (Float) : socket 'Bias' (Bias)
        - brick_width (Float) : socket 'Brick Width' (Brick Width)
        - row_height (Float) : socket 'Row Height' (Row Height)

        Returns
        -------
        - Node: [color (Color), fac (Float)]
        """
        return Node('Brick Texture', {'Vector': vector, 'Color1': color1, 'Color2': color2, 'Mortar': mortar,
            'Scale': scale, 'Mortar Size': mortar_size, 'Mortar Smooth': mortar_smooth, 'Bias': bias, 'Brick Width': brick_width, 'Row Height': row_height})

    @staticmethod
    def Checker(vector=None, color1=None, color2=None, scale=None):
        """ Node 'Checker Texture' (ShaderNodeTexChecker)

        [!Node] Checker Texture

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - color1 (Color) : socket 'Color1' (Color1)
        - color2 (Color) : socket 'Color2' (Color2)
        - scale (Float) : socket 'Scale' (Scale)

        Returns
        -------
        - Node: [color (Color), fac (Float)]
        """
        return Node('Checker Texture', {'Vector': vector, 'Color1': color1, 'Color2': color2, 'Scale': scale})

    @staticmethod
    def Gradient(vector=None):
        """ Node 'Gradient Texture' (ShaderNodeTexGradient)

        [!Node] Gradient Texture

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)

        Returns
        -------
        - Node: [color (Color), fac (Float)]
        """
        return Node('Gradient Texture', {'Vector': vector})

    @staticmethod
    def Image(image=None, vector=None, frame=None, interpolation='Linear', extension='REPEAT'):
        """ Node 'Image Texture' (GeometryNodeImageTexture)

        [!Node] Image Texture

        Arguments
        ---------
        - image (Image) : socket 'Image' (Image)
        - vector (Vector) : socket 'Vector' (Vector)
        - frame (Integer) : socket 'Frame' (Frame)
        - interpolation (str): Node.interpolation in ('Linear', 'Closest', 'Cubic')
        - extension (str): Node.extension in ('REPEAT', 'EXTEND', 'CLIP', 'MIRROR')

        Returns
        -------
        - Node: [color (Color), alpha (Float)]
        """
        return Node('Image Texture', {'Image': image, 'Vector': vector, 'Frame': frame},
            interpolation=interpolation, extension=extension)

    @staticmethod
    def Magic(vector=None, scale=None, distortion=None):
        """ Node 'Magic Texture' (ShaderNodeTexMagic)

        [!Node] Magic Texture

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - scale (Float) : socket 'Scale' (Scale)
        - distortion (Float) : socket 'Distortion' (Distortion)

        Returns
        -------
        - Node: [color (Color), fac (Float)]
        """
        return Node('Magic Texture', {'Vector': vector, 'Scale': scale, 'Distortion': distortion})

    @staticmethod
    def Noise(vector=None, w=None, scale=None, detail=None, roughness=None, lacunarity=None, offset=None, gain=None, distortion=None,
        dim='3D', noise_type='FBM'):
        """ Node 'Noise Texture' (ShaderNodeTexNoise)

        [!Node] Noise Texture

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - w (Float) : socket 'W' (W)
        - scale (Float) : socket 'Scale' (Scale)
        - detail (Float) : socket 'Detail' (Detail)
        - roughness (Float) : socket 'Roughness' (Roughness)
        - lacunarity (Float) : socket 'Lacunarity' (Lacunarity)
        - offset (Float) : socket 'Offset' (Offset)
        - gain (Float) : socket 'Gain' (Gain)
        - distortion (Float) : socket 'Distortion' (Distortion)
        - dim (str): Node.noise_dimensions in ('1D', '2D', '3D', '4D')
        - noise_type (str): Node.noise_type in ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN')

        Returns
        -------
        - Node: [fac (Float), color (Color)]
        """
        return Node('Noise Texture', {'Vector': vector, 'W': w, 'Scale': scale, 'Detail': detail,
            'Roughness': roughness, 'Lacunarity': lacunarity, 'Offset': offset,
            'Gain': gain, 'Distortion': distortion}, noise_dimensions=dim, noise_type=noise_type)

    @staticmethod
    def Voronoi(vector=None, w=None, scale=None, detail=None, roughness=None, lacunarity=None, smoothness=None,
        exponent=None, randomness=None, dim='3D', feature='F1', distance='EUCLIDEAN'):
        """ Node 'Voronoi Texture' (ShaderNodeTexVoronoi)

        [!Node] Voronoi Texture

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - w (Float) : socket 'W' (W)
        - scale (Float) : socket 'Scale' (Scale)
        - detail (Float) : socket 'Detail' (Detail)
        - roughness (Float) : socket 'Roughness' (Roughness)
        - lacunarity (Float) : socket 'Lacunarity' (Lacunarity)
        - smoothness (Float) : socket 'Smoothness' (Smoothness)
        - exponent (Float) : socket 'Exponent' (Exponent)
        - randomness (Float) : socket 'Randomness' (Randomness)
        - distance (str): Node.distance in ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI')
        - feature (str): Node.feature in ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS')
        - dim (str): Node.voronoi_dimensions in ('1D', '2D', '3D', '4D')

        Returns
        -------
        - Node: [distance (Float), color (Color), position (Vector), w (Float), radius (Float)]
        """
        return Node('Voronoi Texture', {'Vector': vector, 'W': w, 'Scale': scale, 'Detail': detail, 'Roughness': roughness,
            'Lacunarity': lacunarity, 'Smoothness': smoothness, 'Exponent': exponent, 'Randomness': randomness},
            voronoi_dimensions=dim, feature=feature, distance=distance)

    @staticmethod
    def Wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None,
        wave_type = 'BANDS', bands_direction='X', rings_direction='X', wave_profile='SIN'):
        """ Node 'Wave Texture' (ShaderNodeTexWave)

        [!Node] Wave Texture

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - scale (Float) : socket 'Scale' (Scale)
        - distortion (Float) : socket 'Distortion' (Distortion)
        - detail (Float) : socket 'Detail' (Detail)
        - detail_scale (Float) : socket 'Detail Scale' (Detail Scale)
        - detail_roughness (Float) : socket 'Detail Roughness' (Detail Roughness)
        - phase_offset (Float) : socket 'Phase Offset' (Phase Offset)
        - bands_direction (str): Node.bands_direction in ('X', 'Y', 'Z', 'DIAGONAL')
        - rings_direction (str): Node.rings_direction in ('X', 'Y', 'Z', 'SPHERICAL')
        - wave_profile (str): Node.wave_profile in ('SIN', 'SAW', 'TRI')
        - wave_type (str): Node.wave_type in ('BANDS', 'RINGS')

        Returns
        -------
        - Node: [color (Color), fac (Float)]
        """
        return Node('Wave Texture', {'Vector': vector, 'Scale': scale, 'Distortion': distortion, 'Detail': detail,
            'Detail Scale': detail_scale, 'Detail Roughness': detail_roughness, 'Phase Offset': phase_offset},
            wave_type=wave_type, bands_direction=bands_direction, wave_profile=wave_profile)

    @staticmethod
    def WhiteNoise(vector=None, w=None, dim='3D'):
        """ Node 'White Noise Texture' (ShaderNodeTexWhiteNoise)

        [!Node] White Noise Texture

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (Vector)
        - w (Float) : socket 'W' (W)
        - dim (str): Node.noise_dimensions in ('1D', '2D', '3D', '4D')

        Returns
        -------
        - Node: [value (Float), color (Color)]
        """
        return Node('White Noise Texture', {'Vector': vector, 'W': w}, noise_dimensions=dim)
