[
    {
        "id": 50,
        "name": "辅助图层",
        "type": "group",
        "opacity": 1
    },
    {
        "pid": 50,
        "type": "graticule",
        "name": "经纬网",
        "id": 24,
        "opacity": 1,
        "zIndex": 23
    },
    {
        "pid": 50,
        "name": "行政区划界线",
        "type": "tdt",
        "layer": "xzqh",
        "mapSplit": false,
        "id": 25,
        "opacity": 1,
        "zIndex": 24
    },
    {
        "pid": 50,
        "name": "高德实时路况",
        "type": "gaode",
        "layer": "time",
        "minimumTerrainLevel": 4,
        "minimumLevel": 4,
        "proxy": "//server.mars3d.cn/proxy/",
        "mapSplit": false,
        "id": 26,
        "opacity": 1,
        "zIndex": 25
    },
    {
        "pid": 50,
        "name": "百度实时路况",
        "type": "baidu",
        "layer": "time",
        "mapSplit": false,
        "id": 27,
        "opacity": 1,
        "zIndex": 26
    },
    {
        "id": 60,
        "name": "地形",
        "type": "group",
        "opacity": 1
    },
    {
        "pid": 60,
        "type": "terrain",
        "name": "Cesium地形",
        "terrainType": "ion",
        "radio": true,
        "id": 28,
        "opacity": 1,
        "zIndex": 28
    },
    {
        "pid": 60,
        "type": "terrain",
        "name": "Mars3D地形",
        "terrainType": "xyz",
        "url": "{mars3d_data}/terrain",
        "radio": true,
        "id": 29,
        "opacity": 1,
        "zIndex": 29
    },
    {
        "pid": 60,
        "type": "terrain",
        "name": "ArcGIS地形",
        "terrainType": "arcgis",
        "url": "https://elevation3d.arcgis.com/arcgis/rest/services/WorldElevation3D/Terrain3D/ImageServer",
        "radio": true,
        "id": 31,
        "opacity": 1,
        "zIndex": 30
    },
    {
        "pid": 60,
        "type": "terrain",
        "name": "无地形",
        "terrainType": "none",
        "radio": true,
        "id": 32,
        "opacity": 1,
        "zIndex": 31
    },
    {
        "id": 40,
        "name": "栅格数据",
        "type": "group",
        "opacity": 1
    },
    {
        "id": 4020,
        "pid": 40,
        "name": "OGC WMS服务",
        "type": "group",
        "opacity": 1
    },
    {
        "pid": 4020,
        "name": "教育设施点",
        "type": "wms",
        "url": "//server.mars3d.cn/geoserver/mars/wms",
        "layers": "mars:hfjy",
        "crs": "EPSG:4326",
        "parameters": {
            "transparent": "true",
            "format": "image/png"
        },
        "popup": "名称：{项目名称}<br />类型：{设施类型}<br />面积：{用地面积}亩<br />位置：{具体位置}",
        "mapSplit": false,
        "flyTo": true,
        "id": 33,
        "opacity": 1,
        "zIndex": 34
    },
    {
        "pid": 4020,
        "name": "道路线",
        "type": "wms",
        "url": "//server.mars3d.cn/geoserver/mars/wms",
        "layers": "mars:hfdl",
        "crs": "EPSG:4326",
        "parameters": {
            "transparent": "true",
            "format": "image/png"
        },
        "center": {
            "lat": 31.743214,
            "lng": 117.277097,
            "alt": 47197.7,
            "heading": 0.3,
            "pitch": -78.8
        },
        "popup": "all",
        "mapSplit": false,
        "flyTo": true,
        "id": 34,
        "opacity": 1,
        "zIndex": 35
    },
    {
        "pid": 4020,
        "name": "建筑物面",
        "type": "wms",
        "url": "//server.mars3d.cn/geoserver/mars/wms",
        "layers": "mars:hfjzw",
        "crs": "EPSG:4326",
        "parameters": {
            "transparent": "true",
            "format": "image/png"
        },
        "highlight": {
            "showTime": 5000,
            "fill": true,
            "color": "#2deaf7",
            "opacity": 0.6,
            "outline": true,
            "outlineWidth": 3,
            "outlineColor": "#e000d9",
            "outlineOpacity": 1,
            "clampToGround": true
        },
        "center": {
            "lat": 31.79513,
            "lng": 117.236172,
            "alt": 3784.6,
            "heading": 0.7,
            "pitch": -42.2
        },
        "popup": "all",
        "flyTo": true,
        "id": 35,
        "opacity": 1,
        "zIndex": 36
    },
    {
        "pid": 4020,
        "name": "规划面",
        "type": "wms",
        "url": "//server.mars3d.cn/geoserver/mars/wms",
        "layers": "mars:hfgh",
        "crs": "EPSG:4326",
        "parameters": {
            "transparent": "true",
            "format": "image/png"
        },
        "center": {
            "lat": 31.743214,
            "lng": 117.277097,
            "alt": 47197.7,
            "heading": 0.3,
            "pitch": -78.8
        },
        "popup": "all",
        "flyTo": true,
        "id": 36,
        "opacity": 1,
        "zIndex": 37
    },
    {
        "id": 4030,
        "pid": 40,
        "name": "ArcGIS 瓦片",
        "type": "group",
        "opacity": 1
    },
    {
        "pid": 4030,
        "name": "合肥规划图",
        "type": "arcgis_cache",
        "url": "{mars3d_data}/arcgis_cache/hfgh/_alllayers/{z}/{y}/{x}.png",
        "minimumLevel": 1,
        "maximumLevel": 17,
        "minimumTerrainLevel": 1,
        "maximumTerrainLevel": 17,
        "rectangle": {
            "xmin": 116.846,
            "xmax": 117.642,
            "ymin": 31.533,
            "ymax": 32.185
        },
        "id": 37,
        "opacity": 1,
        "zIndex": 39
    },
    {
        "id": 4010,
        "pid": 40,
        "name": "ArcGIS Dynamic",
        "type": "group",
        "opacity": 1
    },
    {
        "id": 401085,
        "pid": 4010,
        "type": "arcgis",
        "name": "主要道路",
        "url": "//server.mars3d.cn/arcgis/rest/services/mars/hefei/MapServer",
        "layers": "24",
        "highlight": {
            "type": "polyline",
            "color": "#2deaf7",
            "width": 4,
            "clampToGround": true
        },
        "center": {
            "lat": 31.814176,
            "lng": 117.225362,
            "alt": 5105.3,
            "heading": 359.2,
            "pitch": -83.1
        },
        "popup": "all",
        "mapSplit": false,
        "opacity": 1,
        "zIndex": 41
    },
    {
        "id": 401086,
        "pid": 4010,
        "type": "arcgis",
        "name": "建筑物",
        "url": "//server.mars3d.cn/arcgis/rest/services/mars/hefei/MapServer",
        "layers": "35,36,37,39",
        "highlight": {
            "fill": true,
            "color": "#2deaf7",
            "opacity": 0.6,
            "outline": true,
            "outlineWidth": 3,
            "outlineColor": "#e000d9",
            "outlineOpacity": 1,
            "clampToGround": true
        },
        "center": {
            "lat": 31.816951,
            "lng": 117.22898,
            "alt": 2916.7,
            "heading": 0.3,
            "pitch": -78.8
        },
        "popup": "名称：{NAME}<br />层数：{floor}",
        "opacity": 1,
        "zIndex": 42
    },
    {
        "id": 401087,
        "pid": 4010,
        "type": "arcgis",
        "name": "规划",
        "url": "//server.mars3d.cn/arcgis/rest/services/mars/guihua/MapServer",
        "highlight": {
            "showTime": 5000,
            "fill": true,
            "color": "#2deaf7",
            "opacity": 0.6,
            "outline": true,
            "outlineWidth": 3,
            "outlineColor": "#e000d9",
            "outlineOpacity": 1,
            "clampToGround": true
        },
        "center": {
            "lat": 31.816951,
            "lng": 117.22898,
            "alt": 2916.7,
            "heading": 0.3,
            "pitch": -78.8
        },
        "popup": [
            {
                "field": "用地名称",
                "name": "名称"
            },
            {
                "field": "用地编号",
                "name": "编号"
            },
            {
                "field": "规划用地",
                "name": "规划"
            },
            {
                "type": "html",
                "html": "<div style='text-align: right;color: #ff0000;padding-right: 10px;'>数据仅供参考</div>"
            }
        ],
        "popupNoTitle": true,
        "opacity": 1,
        "zIndex": 43
    },
    {
        "id": 30,
        "name": "矢量数据",
        "type": "group",
        "opacity": 1
    },
    {
        "id": 3030,
        "pid": 30,
        "name": "GeoJSON数据",
        "type": "group",
        "opacity": 1
    },
    {
        "id": 303011,
        "pid": 3030,
        "type": "geojson",
        "name": "平台标绘",
        "url": "{mars3d_data}/file/geojson/mars3d-draw.json",
        "popup": "{type}{name}",
        "flyTo": true,
        "opacity": 1,
        "zIndex": 46
    },
    {
        "pid": 3030,
        "type": "geojson",
        "name": "用地规划",
        "url": "{mars3d_data}/file/geojson/guihua.json",
        "symbol": {
            "styleOptions": {
                "opacity": 0.6,
                "color": "#0000FF",
                "width": 3,
                "clampToGround": true
            },
            "styleField": "类型",
            "styleFieldOptions": {
                "一类居住用地": {
                    "color": "#FFDF7F"
                },
                "二类居住用地": {
                    "color": "#FFFF00"
                },
                "社区服务用地": {
                    "color": "#FF6A38"
                },
                "幼托用地": {
                    "color": "#FF6A38"
                },
                "商住混合用地": {
                    "color": "#FF850A"
                },
                "行政办公用地": {
                    "color": "#FF00FF"
                },
                "文化设施用地": {
                    "color": "#FF00FF"
                },
                "小学用地": {
                    "color": "#FF7FFF"
                },
                "初中用地": {
                    "color": "#FF7FFF"
                },
                "体育场用地": {
                    "color": "#00A57C"
                },
                "医院用地": {
                    "color": "#A5527C"
                },
                "社会福利用地": {
                    "color": "#FF7F9F"
                },
                "商业用地": {
                    "color": "#FF0000"
                },
                "商务用地": {
                    "color": "#7F0000"
                },
                "营业网点用地": {
                    "color": "#FF7F7F"
                },
                "一类工业用地": {
                    "color": "#A57C52"
                },
                "社会停车场用地": {
                    "color": "#C0C0C0"
                },
                "通信用地": {
                    "color": "#007CA5"
                },
                "排水用地": {
                    "color": "#00BFFF"
                },
                "公园绿地": {
                    "color": "#00FF00"
                },
                "防护绿地": {
                    "color": "#007F00"
                },
                "河流水域": {
                    "color": "#7FFFFF"
                },
                "配建停车场": {
                    "color": "#ffffff"
                },
                "道路用地": {
                    "color": "#ffffff"
                }
            }
        },
        "popup": "{类型}",
        "flyTo": true,
        "id": 38,
        "opacity": 1,
        "zIndex": 47
    },
    {
        "pid": 3030,
        "type": "geojson",
        "name": "建筑物面",
        "url": "{mars3d_data}/file/geojson/buildings-demo.json",
        "symbol": {
            "styleOptions": {
                "color": "#0d3685",
                "outlineColor": "#0d3685",
                "opacity": 0.8
            }
        },
        "buildings": {
            "cloumn": "floors",
            "height": "flo_height"
        },
        "popup": "all",
        "flyTo": true,
        "flyToOptions": {
            "minHeight": 2000
        },
        "id": 39,
        "opacity": 1,
        "zIndex": 48
    },
    {
        "pid": 3030,
        "type": "geojson",
        "name": "安徽各市",
        "url": "{mars3d_data}/file/geojson/areas/340000_full.json",
        "symbol": {
            "type": "polygon",
            "styleOptions": {
                "materialType": "PolyGradient",
                "materialOptions": {
                    "color": "rgb(15,176,255)",
                    "opacity": 0.7,
                    "alphaPower": 1.3
                },
                "label": {
                    "text": "{name}",
                    "opacity": 1,
                    "font_size": 25,
                    "color": "#ffffff",
                    "outline": true,
                    "outlineColor": "#000000",
                    "outlineWidth": 3,
                    "scaleByDistance": true,
                    "scaleByDistance_far": 2743804,
                    "scaleByDistance_farValue": 0.3,
                    "scaleByDistance_near": 10000,
                    "scaleByDistance_nearValue": 1,
                    "distanceDisplayCondition": true,
                    "distanceDisplayCondition_far": 2743804,
                    "distanceDisplayCondition_near": 0
                }
            }
        },
        "popup": "{name}",
        "flyTo": true,
        "id": 41,
        "opacity": 1,
        "zIndex": 49
    },
    {
        "pid": 3030,
        "type": "geojson",
        "name": "中国省界",
        "url": "{mars3d_data}/file/geojson/areas/100000_full.json",
        "symbol": {
            "type": "polylineP",
            "styleOptions": {
                "color": "#ffffff",
                "width": 2,
                "opacity": 0.8,
                "label": {
                    "text": "{name}",
                    "position": "center",
                    "font_size": 30,
                    "color": "#ffffff",
                    "outline": true,
                    "outlineColor": "#000000",
                    "scaleByDistance": true,
                    "scaleByDistance_far": 60000000,
                    "scaleByDistance_farValue": 0.2,
                    "scaleByDistance_near": 1000000,
                    "scaleByDistance_nearValue": 1,
                    "distanceDisplayCondition": true,
                    "distanceDisplayCondition_far": 12000000,
                    "distanceDisplayCondition_near": 0
                }
            }
        },
        "flyTo": true,
        "id": 42,
        "opacity": 1,
        "zIndex": 50
    },
    {
        "pid": 3030,
        "type": "geojson",
        "name": "西藏垭口",
        "url": "{mars3d_data}/file/geojson/xizangyakou.json",
        "symbol": {
            "styleOptions": {
                "image": "https://data.mars3d.cn/img/marker/mark-red.png",
                "scaleByDistance": true,
                "scaleByDistance_far": 5000000,
                "scaleByDistance_farValue": 0.5,
                "scaleByDistance_near": 1000,
                "scaleByDistance_nearValue": 1,
                "verticalOrigin": 1,
                "horizontalOrigin": 0,
                "clampToGround": true,
                "label": {
                    "text": "{NAME}",
                    "font_size": 25,
                    "color": "#ffff00",
                    "font_family": "微软雅黑",
                    "outline": true,
                    "outlineColor": "#000000",
                    "pixelOffsetY": -40,
                    "scaleByDistance": true,
                    "scaleByDistance_far": 1000000,
                    "scaleByDistance_farValue": 0.5,
                    "scaleByDistance_near": 1000,
                    "scaleByDistance_nearValue": 1,
                    "distanceDisplayCondition": true,
                    "distanceDisplayCondition_far": 1000000,
                    "distanceDisplayCondition_near": 0,
                    "visibleDepth": true
                }
            }
        },
        "popup": [
            {
                "field": "NAME",
                "name": "名称"
            },
            {
                "type": "details",
                "callback": "showPopupDetails",
                "field": "图片",
                "className": "mars3d-popup-btn-custom"
            }
        ],
        "flyTo": true,
        "id": 43,
        "opacity": 1,
        "zIndex": 51
    },
    {
        "pid": 3030,
        "type": "geojson",
        "name": "体育设施点",
        "url": "{mars3d_data}/file/geojson/hfty-point.json",
        "symbol": {
            "styleOptions": {
                "image": "https://data.mars3d.cn/img/marker/mark-red.png",
                "scale": 1,
                "scaleByDistance": true,
                "scaleByDistance_far": 20000,
                "scaleByDistance_farValue": 0.5,
                "scaleByDistance_near": 1000,
                "scaleByDistance_nearValue": 1,
                "verticalOrigin": 1,
                "horizontalOrigin": 0,
                "clampToGround": true,
                "label": {
                    "text": "{项目名称}",
                    "font_size": 25,
                    "color": "#ffffff",
                    "outline": true,
                    "outlineColor": "#000000",
                    "pixelOffsetY": -25,
                    "scaleByDistance": true,
                    "scaleByDistance_far": 80000,
                    "scaleByDistance_farValue": 0.5,
                    "scaleByDistance_near": 1000,
                    "scaleByDistance_nearValue": 1,
                    "distanceDisplayCondition": true,
                    "distanceDisplayCondition_far": 80000,
                    "distanceDisplayCondition_near": 0
                }
            }
        },
        "popup": [
            {
                "field": "项目名称",
                "name": "项目名称"
            },
            {
                "field": "建设性质",
                "name": "建设性质"
            },
            {
                "field": "设施级别",
                "name": "设施级别"
            },
            {
                "field": "所属区县",
                "name": "所属区县"
            },
            {
                "field": "建筑内容及",
                "name": "建筑内容"
            },
            {
                "field": "新增用地（",
                "name": "新增用地"
            },
            {
                "field": "开工",
                "name": "开工"
            },
            {
                "field": "总投资（万",
                "name": "总投资"
            },
            {
                "field": "资金来源",
                "name": "资金来源"
            },
            {
                "field": "初步选址",
                "name": "初步选址"
            },
            {
                "field": "设施类型",
                "name": "设施类型"
            },
            {
                "field": "设施等级",
                "name": "设施等级"
            },
            {
                "field": "所在区县",
                "name": "所在区县"
            },
            {
                "field": "具体位置",
                "name": "具体位置"
            },
            {
                "field": "建设内容（",
                "name": "建设内容"
            },
            {
                "field": "用地面积（",
                "name": "用地面积",
                "format": "mars3d.MeasureUtil.formatArea"
            },
            {
                "field": "设施规模（",
                "name": "设施规模"
            },
            {
                "field": "举办者类型",
                "name": "举办者类型"
            },
            {
                "field": "开工时间",
                "name": "开工时间"
            },
            {
                "field": "总投资额（",
                "name": "总投资额",
                "unit": "亿元"
            },
            {
                "field": "项目推进主",
                "name": "项目推进主体"
            },
            {
                "field": "项目进度",
                "name": "项目进度"
            },
            {
                "field": "项目来源",
                "name": "项目来源"
            },
            {
                "field": "备注",
                "name": "备注"
            }
        ],
        "flyTo": true,
        "id": 44,
        "opacity": 1,
        "zIndex": 52
    },
    {
        "id": 3070,
        "pid": 30,
        "name": "GeoServer WFS",
        "type": "group",
        "opacity": 1
    },
    {
        "pid": 3070,
        "type": "wfs",
        "name": "建筑物面",
        "url": "//server.mars3d.cn/geoserver/mars/ows",
        "layer": "mars:hfjzw",
        "parameters": {
            "maxFeatures": 500
        },
        "minimumLevel": 15,
        "symbol": {
            "type": "polygonP",
            "styleOptions": {
                "color": "#00469c",
                "outline": false,
                "opacity": 1
            }
        },
        "buildings": {
            "cloumn": "floor"
        },
        "center": {
            "lat": 31.818396,
            "lng": 117.229083,
            "alt": 2554.4,
            "heading": 359.2,
            "pitch": -83.1
        },
        "popup": "名称：{NAME}<br />层数：{floor}",
        "id": 45,
        "opacity": 1,
        "IdField": "id",
        "zIndex": 54
    },
    {
        "pid": 3070,
        "name": "教育设施点",
        "type": "wfs",
        "url": "//server.mars3d.cn/geoserver/mars/ows",
        "layer": "mars:hfjy",
        "parameters": {
            "maxFeatures": 500
        },
        "minimumLevel": 13,
        "symbol": {
            "type": "billboardP",
            "styleOptions": {
                "image": "https://data.mars3d.cn/img/marker/mark-red.png",
                "scaleByDistance": true,
                "scaleByDistance_far": 20000,
                "scaleByDistance_farValue": 0.6,
                "scaleByDistance_near": 1000,
                "scaleByDistance_nearValue": 1,
                "clampToGround": true,
                "label": {
                    "text": "{项目名称}",
                    "font_size": 15,
                    "color": "#ffffff",
                    "outline": true,
                    "outlineColor": "#000000",
                    "pixelOffsetY": -30,
                    "distanceDisplayCondition": true,
                    "distanceDisplayCondition_far": 2000,
                    "distanceDisplayCondition_near": 0
                }
            }
        },
        "center": {
            "lat": 31.812256,
            "lng": 117.229873,
            "alt": 4683.91,
            "heading": 357.4,
            "pitch": -65.4
        },
        "popup": "all",
        "id": 46,
        "opacity": 1,
        "IdField": "id",
        "zIndex": 55
    },
    {
        "id": 3010,
        "pid": 30,
        "name": "ArcGIS WFS",
        "type": "group",
        "opacity": 1
    },
    {
        "pid": 3010,
        "type": "arcgis_wfs",
        "name": "兴趣点",
        "url": "//server.mars3d.cn/arcgis/rest/services/mars/hefei/MapServer/1",
        "where": " 1=1 ",
        "minimumLevel": 15,
        "center": {
            "lat": 31.818396,
            "lng": 117.229083,
            "alt": 2554.4,
            "heading": 359.2,
            "pitch": -83.1
        },
        "symbol": {
            "type": "billboardP",
            "styleOptions": {
                "image": "https://data.mars3d.cn/img/marker/mark-blue.png",
                "scaleByDistance": true,
                "scaleByDistance_far": 20000,
                "scaleByDistance_farValue": 0.6,
                "scaleByDistance_near": 1000,
                "scaleByDistance_nearValue": 1,
                "clampToGround": true,
                "label": {
                    "text": "{NAME}",
                    "font_size": 15,
                    "color": "#ffffff",
                    "outline": true,
                    "outlineColor": "#000000",
                    "pixelOffsetY": -30,
                    "distanceDisplayCondition": true,
                    "distanceDisplayCondition_far": 3000,
                    "distanceDisplayCondition_near": 0
                }
            },
            "styleField": "address",
            "styleFieldOptions": {
                "AB03": {
                    "image": "https://data.mars3d.cn/img/marker/mark-red.png"
                },
                "A980": {
                    "image": "https://data.mars3d.cn/img/marker/mark-blue.png"
                },
                "A900": {
                    "image": "https://data.mars3d.cn/img/marker/mark-green.png"
                }
            }
        },
        "popup": "名称：{NAME}<br />地址：{address}",
        "id": 47,
        "opacity": 1,
        "IdField": "id",
        "zIndex": 57
    },
    {
        "pid": 3010,
        "type": "arcgis_wfs",
        "name": "道路",
        "url": "//server.mars3d.cn/arcgis/rest/services/mars/hefei/MapServer/28",
        "minimumLevel": 14,
        "symbol": {
            "type": "polylineP",
            "styleOptions": {
                "color": "#3388ff",
                "width": 3,
                "clampToGround": true
            },
            "styleField": "NAME",
            "styleFieldOptions": {
                "祁门路": {
                    "color": "#8744c0",
                    "width": 3
                },
                "东流路": {
                    "color": "#f7ba2a",
                    "width": 3
                },
                "翡翠路": {
                    "color": "#20a0ff",
                    "width": 3
                },
                "岳西路": {
                    "color": "#50bfff",
                    "width": 3
                }
            }
        },
        "popup": "名称：{NAME}",
        "center": {
            "lat": 31.814176,
            "lng": 117.225362,
            "alt": 5105.3,
            "heading": 359.2,
            "pitch": -83.1
        },
        "id": 48,
        "opacity": 1,
        "IdField": "id",
        "zIndex": 58
    },
    {
        "pid": 3010,
        "type": "arcgis_wfs",
        "name": "建筑物面",
        "url": "//server.mars3d.cn/arcgis/rest/services/mars/hefei/MapServer/37",
        "minimumLevel": 15,
        "symbol": {
            "styleOptions": {
                "color": "#0d3685",
                "outlineColor": "#0d3685",
                "opacity": 0.8
            }
        },
        "buildings": {
            "cloumn": "floor"
        },
        "debuggerTileInfo": false,
        "center": {
            "lat": 31.816951,
            "lng": 117.22898,
            "alt": 1916.7,
            "heading": 0.3,
            "pitch": -78.8
        },
        "popup": "名称：{NAME}<br />层数：{floor}",
        "id": 49,
        "opacity": 1,
        "IdField": "id",
        "zIndex": 59
    },
    {
        "id": 3060,
        "pid": 30,
        "name": "CZML数据",
        "type": "group",
        "opacity": 1
    },
    {
        "id": 306010,
        "pid": 3060,
        "type": "czml",
        "name": "汽车",
        "url": "{mars3d_data}/file/czml/car.czml",
        "center": {
            "lat": 40.894745,
            "lng": 121.920252,
            "alt": 904,
            "heading": 64,
            "pitch": -67
        },
        "radio": true,
        "flyTo": true,
        "opacity": 1,
        "zIndex": 61
    },
    {
        "id": 306011,
        "pid": 3060,
        "type": "czml",
        "name": "卫星轨道",
        "url": "{mars3d_data}/file/czml/satellite-simple.czml",
        "popup": "all",
        "radio": true,
        "flyTo": true,
        "opacity": 1,
        "zIndex": 62
    },
    {
        "id": 3050,
        "pid": 30,
        "name": "KML数据",
        "type": "group",
        "opacity": 1
    },
    {
        "pid": 3050,
        "type": "kml",
        "name": "海上安全警告",
        "url": "{mars3d_data}/file/kml/NAVWARN.kmz",
        "popup": "all",
        "id": 51,
        "opacity": 1,
        "zIndex": 64
    },
    {
        "pid": 3050,
        "type": "kml",
        "name": "国境线",
        "url": "{mars3d_data}/file/kml/countryboundary.kml",
        "symbol": {
            "styleOptions": {
                "color": "#FED976",
                "width": 2
            }
        },
        "id": 52,
        "opacity": 1,
        "fill": {
            "red": 0.996078431372549,
            "green": 0.8509803921568627,
            "blue": 0.4627450980392157,
            "alpha": 0.5
        },
        "zIndex": 65
    },
    {
        "pid": 3050,
        "type": "kml",
        "name": "省界线",
        "url": "{mars3d_data}/file/kml/province.kml",
        "symbol": {
            "styleOptions": {
                "color": "#00FF00",
                "width": 2
            }
        },
        "id": 53,
        "opacity": 1,
        "fill": {
            "red": 0,
            "green": 1,
            "blue": 0,
            "alpha": 0.5
        },
        "zIndex": 66
    },
    {
        "id": 20,
        "name": "三维模型",
        "type": "group",
        "opacity": 1
    },
    {
        "id": 2010,
        "pid": 20,
        "name": "gltf模型",
        "type": "group",
        "opacity": 1
    },
    {
        "pid": 2010,
        "type": "graphic",
        "name": "风力发电机",
        "data": [
            {
                "type": "modelP",
                "position": [
                    117.219071,
                    31.828783,
                    39.87
                ],
                "style": {
                    "url": "https://data.mars3d.cn/gltf/mars/fengche.gltf",
                    "scale": 50,
                    "heading": -93
                }
            }
        ],
        "popup": "示例信息，这是一个风力发电机",
        "center": {
            "lat": 31.821083,
            "lng": 117.21832,
            "alt": 832.64,
            "heading": 2.3,
            "pitch": -39.2
        },
        "id": 54,
        "opacity": 1,
        "zIndex": 69
    },
    {
        "pid": 2010,
        "type": "graphic",
        "name": "警车",
        "data": [
            {
                "type": "modelP",
                "position": [
                    117.217458,
                    31.815349,
                    35.03
                ],
                "style": {
                    "url": "https://data.mars3d.cn/gltf/mars/jingche/jingche.gltf",
                    "scale": 2,
                    "heading": -95,
                    "clampToGround": true
                }
            }
        ],
        "center": {
            "lat": 31.815363,
            "lng": 117.215958,
            "alt": 107.35,
            "heading": 90.7,
            "pitch": -26.1
        },
        "id": 55,
        "opacity": 1,
        "zIndex": 70
    },
    {
        "id": 2040,
        "pid": 20,
        "name": "城市白模",
        "type": "group",
        "opacity": 1
    },
    {
        "id": 204011,
        "pid": 2040,
        "type": "tileset",
        "name": "合肥市区",
        "url": "{mars3d_data}/3dtiles/jzw-hefei/tileset.json",
        "maximumScreenSpaceError": 1,
        "maxMemory": 1024,
        "style": {
            "color": {
                "conditions": [
                    [
                        "true",
                        "color('rgba(42, 160, 224, 1)')"
                    ]
                ]
            }
        },
        "marsJzwStyle": true,
        "highlight": {
            "type": "click",
            "color": "#FFFF00"
        },
        "popup": [
            {
                "field": "objectid",
                "name": "编号"
            },
            {
                "field": "name",
                "name": "名称"
            },
            {
                "field": "height",
                "name": "楼高",
                "unit": "米"
            }
        ],
        "center": {
            "lat": 31.786281,
            "lng": 117.223716,
            "alt": 3718,
            "heading": 2,
            "pitch": -45
        },
        "opacity": 1,
        "zIndex": 72
    },
    {
        "pid": 2040,
        "type": "tileset",
        "name": "合肥市区-带贴图",
        "url": "{mars3d_data}/3dtiles/jzw-hefei-cz/tileset.json",
        "maximumScreenSpaceError": 1,
        "maxMemory": 1024,
        "marsJzwStyle": true,
        "highlight": {
            "type": "click",
            "color": "#FFFF00"
        },
        "popup": [
            {
                "field": "objectid",
                "name": "编号"
            },
            {
                "field": "remark",
                "name": "名称"
            },
            {
                "field": "height",
                "name": "楼高",
                "unit": "米"
            }
        ],
        "center": {
            "lat": 31.786281,
            "lng": 117.223716,
            "alt": 3718,
            "heading": 2,
            "pitch": -45
        },
        "id": 56,
        "opacity": 1,
        "zIndex": 73
    },
    {
        "id": 204012,
        "pid": 2040,
        "type": "tileset",
        "name": "上海市区",
        "url": "{mars3d_data}/3dtiles/jzw-shanghai/tileset.json",
        "maximumScreenSpaceError": 4,
        "maxMemory": 2048,
        "style": {
            "color": {
                "conditions": [
                    [
                        "${floor} >= 200",
                        "rgba(45, 0, 75, 0.5)"
                    ],
                    [
                        "${floor} >= 100",
                        "rgb(170, 162, 204)"
                    ],
                    [
                        "${floor} >= 50",
                        "rgb(224, 226, 238)"
                    ],
                    [
                        "${floor} >= 25",
                        "rgb(252, 230, 200)"
                    ],
                    [
                        "${floor} >= 10",
                        "rgb(248, 176, 87)"
                    ],
                    [
                        "${floor} >= 5",
                        "rgb(198, 106, 11)"
                    ],
                    [
                        "true",
                        "rgb(127, 59, 8)"
                    ]
                ]
            }
        },
        "highlight": {
            "type": "click",
            "color": "#FFFF00"
        },
        "popup": [
            {
                "field": "name",
                "name": "名称"
            },
            {
                "field": "floor",
                "name": "楼层"
            }
        ],
        "center": {
            "lat": 31.257341,
            "lng": 121.466139,
            "alt": 2170.8,
            "heading": 122.2,
            "pitch": -31.8
        },
        "opacity": 1,
        "zIndex": 74
    },
    {
        "id": 2050,
        "pid": 20,
        "name": "点云",
        "type": "group",
        "opacity": 1
    },
    {
        "id": 202016,
        "pid": 2050,
        "type": "tileset",
        "name": "高压线塔杆",
        "url": "{mars3d_data}/3dtiles/pnts-ganta/tileset.json",
        "maximumScreenSpaceError": 1,
        "position": {
            "alt": 31
        },
        "style": {
            "color": {
                "conditions": [
                    [
                        "(${Classification} >= 4) && (${Classification} < 5) ",
                        "color('#DC143C')"
                    ],
                    [
                        "(${Classification} >= 7) && (${Classification} < 8)  ",
                        "color('#7B68EE')"
                    ],
                    [
                        "(${Classification} >= 16) && (${Classification} < 17)  ",
                        "color('#00CED1')"
                    ],
                    [
                        "(${Classification} >= 17) && (${Classification} < 18)  ",
                        "color('#3CB371')"
                    ],
                    [
                        "(${Classification} >= 18) && (${Classification} < 19)  ",
                        "color('#FFFF00')"
                    ],
                    [
                        "(${Classification} >= 19) && (${Classification} < 20)  ",
                        "color('#FFA500')"
                    ],
                    [
                        "(${Classification} >= 20) && (${Classification} < 21)  ",
                        "color('#FF6347')"
                    ]
                ]
            }
        },
        "hasOpacity": false,
        "center": {
            "lat": 31.504746,
            "lng": 118.264278,
            "alt": 580,
            "heading": 29,
            "pitch": -49
        },
        "opacity": 1,
        "zIndex": 76
    },
    {
        "id": 2060,
        "pid": 20,
        "name": "BIM模型",
        "type": "group",
        "opacity": 1
    },
    {
        "id": 20601121,
        "pid": 2060,
        "type": "tileset",
        "name": "大学教学楼",
        "url": "{mars3d_data}/3dtiles/bim-daxue/tileset.json",
        "position": {
            "lng": 117.251229,
            "lat": 31.844015,
            "alt": 31.2
        },
        "highlight": {
            "type": "click",
            "color": "#FFFF00"
        },
        "popup": "all",
        "scenetree": "scenetree.json",
        "center": {
            "lat": 31.842516,
            "lng": 117.25107,
            "alt": 145,
            "heading": 8,
            "pitch": -39
        },
        "opacity": 1,
        "zIndex": 78
    },
    {
        "pid": 2060,
        "type": "tileset",
        "name": "轻轨地铁站",
        "url": "{mars3d_data}/3dtiles/bim-ditiezhan/tileset.json",
        "position": {
            "lng": 117.203994,
            "lat": 31.857999,
            "alt": 28.9
        },
        "rotation": {
            "z": 168.1
        },
        "maxMemory": 2048,
        "highlight": {
            "type": "click",
            "color": "#00FF00"
        },
        "popup": "all",
        "scenetree": "scenetree.json",
        "center": {
            "lat": 31.856125,
            "lng": 117.204513,
            "alt": 155,
            "heading": 350,
            "pitch": -31
        },
        "id": 57,
        "opacity": 1,
        "zIndex": 79
    },
    {
        "id": 206012,
        "pid": 2060,
        "type": "tileset",
        "name": "桥梁",
        "url": "{mars3d_data}/3dtiles/bim-qiaoliang/tileset.json",
        "position": {
            "lng": 117.096906,
            "lat": 31.851564,
            "alt": 45
        },
        "rotation": {
            "z": 17.5
        },
        "maximumScreenSpaceError": 16,
        "skipLevelOfDetail": true,
        "loadSiblings": true,
        "cullRequestsWhileMoving": true,
        "cullRequestsWhileMovingMultiplier": 10,
        "preferLeaves": true,
        "progressiveResolutionHeightFraction": 0.5,
        "dynamicScreenSpaceError": true,
        "preloadWhenHidden": true,
        "center": {
            "lat": 31.849357,
            "lng": 117.099194,
            "alt": 306.2,
            "heading": 327.1,
            "pitch": -30.9
        },
        "scenetree": "scenetree.json",
        "highlight": {
            "type": "click",
            "color": "#00FF00"
        },
        "popup": "all",
        "opacity": 1,
        "zIndex": 80
    },
    {
        "id": 2020,
        "pid": 20,
        "name": "人工建模",
        "type": "group",
        "opacity": 1
    },
    {
        "id": 202013,
        "pid": 2020,
        "type": "tileset",
        "name": "地下管网",
        "url": "{mars3d_data}/3dtiles/max-piping/tileset.json",
        "position": {
            "lng": 117.215457,
            "lat": 31.843363,
            "alt": -3.6
        },
        "rotation": {
            "z": 336.7
        },
        "maximumScreenSpaceError": 2,
        "highlight": {
            "type": "click",
            "color": "#00FF00"
        },
        "popup": "all",
        "center": {
            "lat": 31.838821,
            "lng": 117.216402,
            "alt": 461,
            "heading": 0,
            "pitch": -46
        },
        "msg": "演示数据，地下数据拖动时会在地面漂移",
        "opacity": 1,
        "zIndex": 82
    },
    {
        "id": 202012,
        "pid": 2020,
        "type": "tileset",
        "name": "石化工厂",
        "url": "{mars3d_data}/3dtiles/max-shihua/tileset.json",
        "position": {
            "lng": 117.077158,
            "lat": 31.659116,
            "alt": -2
        },
        "maximumScreenSpaceError": 1,
        "maxMemory": 2048,
        "highlight": {
            "type": "click",
            "color": "#00FF00"
        },
        "popup": "all",
        "scenetree": "scenetree.json",
        "center": {
            "lat": 31.654916,
            "lng": 117.08278,
            "alt": 279,
            "heading": 316,
            "pitch": -29
        },
        "opacity": 1,
        "zIndex": 83
    },
    {
        "id": 202030,
        "pid": 2020,
        "name": "水利闸门",
        "type": "group",
        "open": false,
        "center": {
            "lat": 29.794301,
            "lng": 121.47998,
            "alt": 262,
            "heading": 191,
            "pitch": -35
        },
        "opacity": 1
    },
    {
        "pid": 202030,
        "name": "闸门",
        "type": "graphic",
        "data": [
            {
                "type": "modelP",
                "position": [
                    121.479813,
                    29.791278,
                    16
                ],
                "style": {
                    "url": "https://data.mars3d.cn/gltf/mars/zhamen.glb",
                    "heading": 105
                }
            }
        ],
        "center": {
            "lat": 29.791607,
            "lng": 121.479925,
            "alt": 27,
            "heading": 198,
            "pitch": -18
        },
        "id": 58,
        "opacity": 1,
        "zIndex": 85
    },
    {
        "id": 202011,
        "pid": 202030,
        "type": "tileset",
        "name": "整体",
        "url": "{mars3d_data}/3dtiles/max-fsdzm/tileset.json",
        "position": {
            "alt": 15.2
        },
        "maximumScreenSpaceError": 1,
        "center": {
            "lat": 29.792675,
            "lng": 121.480207,
            "alt": 190.8,
            "heading": 196.1,
            "pitch": -49
        },
        "opacity": 1,
        "zIndex": 86
    },
    {
        "id": 2030,
        "pid": 20,
        "name": "倾斜摄影",
        "type": "group",
        "opacity": 1
    },
    {
        "pid": 2030,
        "type": "tileset",
        "name": "大雁塔",
        "url": "{mars3d_data}/3dtiles/qx-dyt/tileset.json",
        "position": {
            "alt": -27
        },
        "maximumScreenSpaceError": 1,
        "center": {
            "lat": 34.215516,
            "lng": 108.960251,
            "alt": 834,
            "heading": 4,
            "pitch": -48
        },
        "flat": {
            "enabled": true,
            "editHeight": -24
        },
        "flyTo": false,
        "id": 59,
        "opacity": 1,
        "zIndex": 88
    },
    {
        "pid": 2030,
        "name": "校园(含单体)",
        "type": "group",
        "hasOpacity": true,
        "center": {
            "lat": 43.821193,
            "lng": 125.143124,
            "alt": 990,
            "heading": 342,
            "pitch": -50
        },
        "layers": [
            {
                "type": "geojson",
                "name": "校园-单体化",
                "url": "{mars3d_data}/file/geojson/dth-xuexiao-fd.json",
                "symbol": {
                    "type": "polygonP",
                    "styleOptions": {
                        "color": "rgba(255, 255, 255, 0.01)",
                        "clampToGround": true,
                        "classification": true,
                        "buffer": 1,
                        "highlight": {
                            "type": "click",
                            "color": "rgba(255,255,0,0.4)"
                        }
                    }
                },
                "popup": [
                    {
                        "field": "name",
                        "name": "学校场所"
                    },
                    {
                        "field": "sfkf",
                        "name": "是否开放"
                    },
                    {
                        "field": "remark",
                        "name": "备注信息"
                    }
                ],
                "pid": 61,
                "parent": {
                    "pid": 2030,
                    "name": "校园(含单体)",
                    "type": "group",
                    "hasOpacity": true,
                    "center": {
                        "lat": 43.821193,
                        "lng": 125.143124,
                        "alt": 990,
                        "heading": 342,
                        "pitch": -50
                    },
                    "layers": [
                        {
                            "type": "geojson",
                            "name": "校园-单体化",
                            "url": "{mars3d_data}/file/geojson/dth-xuexiao-fd.json",
                            "symbol": {
                                "type": "polygonP",
                                "styleOptions": {
                                    "color": "rgba(255, 255, 255, 0.01)",
                                    "clampToGround": true,
                                    "classification": true,
                                    "buffer": 1,
                                    "highlight": {
                                        "type": "click",
                                        "color": "rgba(255,255,0,0.4)"
                                    }
                                }
                            },
                            "popup": [
                                {
                                    "field": "name",
                                    "name": "学校场所"
                                },
                                {
                                    "field": "sfkf",
                                    "name": "是否开放"
                                },
                                {
                                    "field": "remark",
                                    "name": "备注信息"
                                }
                            ],
                            "pid": 61,
                            "id": 62,
                            "zIndex": 89
                        },
                        {
                            "pid": 61,
                            "type": "tileset",
                            "name": "校园",
                            "url": "{mars3d_data}/3dtiles/qx-xuexiao/tileset.json",
                            "position": {
                                "alt": 279
                            },
                            "maximumScreenSpaceError": 1,
                            "id": 63,
                            "zIndex": 90
                        }
                    ],
                    "id": 61
                },
                "id": 62,
                "zIndex": 89
            },
            {
                "pid": 61,
                "type": "tileset",
                "name": "校园",
                "url": "{mars3d_data}/3dtiles/qx-xuexiao/tileset.json",
                "position": {
                    "alt": 279
                },
                "maximumScreenSpaceError": 1,
                "parent": {
                    "pid": 2030,
                    "name": "校园(含单体)",
                    "type": "group",
                    "hasOpacity": true,
                    "center": {
                        "lat": 43.821193,
                        "lng": 125.143124,
                        "alt": 990,
                        "heading": 342,
                        "pitch": -50
                    },
                    "layers": [
                        {
                            "type": "geojson",
                            "name": "校园-单体化",
                            "url": "{mars3d_data}/file/geojson/dth-xuexiao-fd.json",
                            "symbol": {
                                "type": "polygonP",
                                "styleOptions": {
                                    "color": "rgba(255, 255, 255, 0.01)",
                                    "clampToGround": true,
                                    "classification": true,
                                    "buffer": 1,
                                    "highlight": {
                                        "type": "click",
                                        "color": "rgba(255,255,0,0.4)"
                                    }
                                }
                            },
                            "popup": [
                                {
                                    "field": "name",
                                    "name": "学校场所"
                                },
                                {
                                    "field": "sfkf",
                                    "name": "是否开放"
                                },
                                {
                                    "field": "remark",
                                    "name": "备注信息"
                                }
                            ],
                            "pid": 61,
                            "id": 62,
                            "zIndex": 89
                        },
                        {
                            "pid": 61,
                            "type": "tileset",
                            "name": "校园",
                            "url": "{mars3d_data}/3dtiles/qx-xuexiao/tileset.json",
                            "position": {
                                "alt": 279
                            },
                            "maximumScreenSpaceError": 1,
                            "id": 63,
                            "zIndex": 90
                        }
                    ],
                    "id": 61
                },
                "id": 63,
                "zIndex": 90
            }
        ],
        "id": 61,
        "opacity": 1
    },
    {
        "id": 203014,
        "pid": 2030,
        "type": "tileset",
        "name": "县城社区",
        "url": "{mars3d_data}/3dtiles/qx-shequ/tileset.json",
        "position": {
            "alt": 148.2
        },
        "maximumScreenSpaceError": 2,
        "dynamicScreenSpaceError": true,
        "cullWithChildrenBounds": false,
        "center": {
            "lat": 28.440864,
            "lng": 119.486477,
            "alt": 588.23,
            "heading": 268.6,
            "pitch": -37.8
        },
        "flyTo": false,
        "opacity": 1,
        "zIndex": 91
    },
    {
        "id": 203015,
        "pid": 2030,
        "name": "合肥天鹅湖",
        "type": "tileset",
        "url": "{mars3d_data}/3dtiles/qx-teh/tileset.json",
        "position": {
            "lng": 117.218434,
            "lat": 31.81807,
            "alt": 163
        },
        "maximumScreenSpaceError": 16,
        "maxMemory": 2048,
        "dynamicScreenSpaceError": true,
        "cullWithChildrenBounds": false,
        "skipLevelOfDetail": true,
        "preferLeaves": true,
        "center": {
            "lat": 31.795308,
            "lng": 117.21948,
            "alt": 1820,
            "heading": 0,
            "pitch": -39
        },
        "opacity": 1,
        "zIndex": 92
    },
    {
        "id": 203013,
        "pid": 2030,
        "type": "geojson",
        "name": "文庙-单体化",
        "url": " {mars3d_data}/file/geojson/dth-wm.json",
        "symbol": {
            "type": "polygonP",
            "styleOptions": {
                "color": "rgba(255, 255, 255, 0.01)",
                "clampToGround": true,
                "classification": true,
                "buffer": 1,
                "highlight": {
                    "color": "rgba(255,255,0,0.4)"
                }
            }
        },
        "popup": [
            {
                "field": "name",
                "name": "房屋名称"
            },
            {
                "field": "jznf",
                "name": "建造年份"
            },
            {
                "field": "ssdw",
                "name": "所属单位"
            },
            {
                "field": "remark",
                "name": "备注信息"
            }
        ],
        "opacity": 1,
        "zIndex": 93
    },
    {
        "id": 203012,
        "pid": 2030,
        "type": "tileset",
        "name": "文庙",
        "url": "{mars3d_data}/3dtiles/qx-simiao/tileset.json",
        "position": {
            "alt": 38.8
        },
        "maximumScreenSpaceError": 2,
        "dynamicScreenSpaceError": true,
        "cullWithChildrenBounds": false,
        "skipLevelOfDetail": true,
        "preferLeaves": true,
        "center": {
            "lat": 33.589536,
            "lng": 119.032216,
            "alt": 145.08,
            "heading": 3.1,
            "pitch": -22.9
        },
        "opacity": 1,
        "zIndex": 94
    },
    {
        "id": 99,
        "name": "数据图层",
        "type": "group",
        "opacity": 1
    }
]