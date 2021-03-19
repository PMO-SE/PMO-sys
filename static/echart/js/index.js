// Workload by Region
(function() {
  // 实例化对象
  var myChart = echarts.init(document.querySelector(".bar .chart"));
  var ctx = document.querySelector(".bar .chart");
  var workloads = ctx.attributes['workload'].value;
  //类型转换
  workloads = workloads.replace(/\'/g, '"')
  workloads = JSON.parse(workloads);
  var a=[];
  for (var workload in workloads) {
    a.push(workloads[workload])
  }
  console.log(workloads);
  a.splice(0,1);
  console.log(a);

  // 指定配置和数据
  var option = {
    color: ["#2f89cf"],
    tooltip: {
      trigger: "axis",
      axisPointer: {
        // 坐标轴指示器，坐标轴触发有效
        type: "shadow" // 默认为直线，可选为：'line' | 'shadow'
      }
    },
    grid: {
      left: "0%",
      top: "10px",
      right: "0%",
      bottom: "4%",
      containLabel: true
    },
    yAxis: [
      {
        inverse:true,
        type: "category",
        data: [
          "2021Q1",
          "2021Q2",
          "2021Q3",
          "2021Q4",
        ],
        axisTick: {
          alignWithLabel: true
        },
        axisLabel: {
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: "12"
          }
        },
        axisLine: {
          show: false
        }
      }
    ],
    xAxis: [
      {
        type: "value",
        axisLabel: {
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: "12"
          }
        },
        axisLine: {
          lineStyle: {
            color: "rgba(255,255,255,.1)"
            // width: 1,
            // type: "solid"
          }
        },
        splitLine: {
          lineStyle: {
            color: "rgba(255,255,255,.1)"
          }
        }
      }
    ],
    series: [
      {
        name: "Workload",
        type: "bar",
        barWidth: "35%",
        data: [33,32,25,20],
        itemStyle: {
          barBorderRadius: 5
        },
        label: {
          show: true,
          position: 'inside'
        },
        markLine:{
          symbol:'none',
          data:[{
            name: 'HC',
            xAxis: 21,

          }],
          color: '#FFFFFF',
          label:{
            show: true,
            position: 'middle',
            textStyle:{
              color:'#FFFFFF'
            },
            formatter: '{b}: {c}',
          },
        }
      }
    ]
  };

  // 把配置给实例对象
  myChart.setOption(option);
  window.addEventListener("resize", function() {
    myChart.resize();
  });

  // 数据变化
  var dataAll = [
    { year: "North", data: [200, 300, 300, 900, 1500, 1200, 600] },
    { year: "South", data: [300, 400, 350, 800, 1800, 1400, 700] },
    { year: "East&West", data: [1344, 1300, 350, 800, 1800, 1400, 700] },
    { year: "Wuxi", data: [300, 13000, 350, 800, 1800, 1400, 700] }
  ];

  $(".bar h2 ").on("click", "a", function() {
    option.series[0].data = dataAll[$(this).index()].data;
    myChart.setOption(option);
  });
})();

// 折线图定制
// (function() {
//   // 基于准备好的dom，初始化echarts实例
//   var myChart = echarts.init(document.querySelector(".line .chart"));
//
//   // (1)准备数据
//   var data = {
//     year: [
//       [21, 21, 21, 21],
//       [24, 27, 31, 1],
//     ]
//   };
//
//   // 2. 指定配置和数据
//   var option = {
//     color: ["#00f2f1", "#ed3f35"],
//     tooltip: {
//       // 通过坐标轴来触发
//       trigger: "axis"
//     },
//     legend: {
//       // 距离容器10%
//       right: "10%",
//       // 修饰图例文字的颜色
//       textStyle: {
//         color: "#4c9bfd"
//       }
//       // 如果series 里面设置了name，此时图例组件的data可以省略
//       // data: ["邮件营销", "联盟广告"]
//     },
//     grid: {
//       top: "20%",
//       left: "3%",
//       right: "4%",
//       bottom: "3%",
//       show: true,
//       borderColor: "#012f4a",
//       containLabel: true
//     },
//
//     xAxis: {
//       type: "category",
//       boundaryGap: false,
//       data: [
//         "2021 Q1",
//         "2021 Q2",
//         "2021 Q3",
//         "2021 Q4",
//       ],
//       // 去除刻度
//       axisTick: {
//         show: false
//       },
//       // 修饰刻度标签的颜色
//       axisLabel: {
//         color: "rgba(255,255,255,.7)"
//       },
//       // 去除x坐标轴的颜色
//       axisLine: {
//         show: false
//       }
//     },
//     yAxis: {
//       type: "value",
//       // 去除刻度
//       axisTick: {
//         show: false
//       },
//       // 修饰刻度标签的颜色
//       axisLabel: {
//         color: "rgba(255,255,255,.7)"
//       },
//       // 修改y轴分割线的颜色
//       splitLine: {
//         lineStyle: {
//           color: "#012f4a"
//         }
//       }
//     },
//     series: [
//       {
//         name: "新增粉丝",
//         type: "line",
//         stack: "总量",
//         // 是否让线条圆滑显示
//         smooth: true,
//         data: data.year[0]
//       },
//       {
//         name: "新增游客",
//         type: "line",
//         stack: "总量",
//         smooth: true,
//         data: data.year[1]
//       }
//     ]
//   };
//   // 3. 把配置和数据给实例对象
//   myChart.setOption(option);
//
//   // 重新把配置好的新数据给实例对象
//   myChart.setOption(option);
//   window.addEventListener("resize", function() {
//     myChart.resize();
//   });
// })();

// COGS by BU
(function() {
  // 1. 实例化对象
  var myChart = echarts.init(document.querySelector(".line  .chart"));
  var ctx = document.querySelector(".line .chart");
  var myBUs = ctx.attributes['myBUs'].value;
  var mydata = ctx.attributes['mydata'].value;
  //类型转换
  console.log(myBUs)
  console.log(mydata)
  var myBUs = eval(myBUs);
  var mydata = eval(mydata);
  var i = 0;
//构造data数据
len = mydata.length;
var array = [];
for(;i<len;i++){
    array.push({value:mydata[i],name:myBUs[i]});
};
  // 2. 指定配置项和数据
  var option = {
    legend: {
      top: "90%",
      itemWidth: 10,
      itemHeight: 10,
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "12"
      }
    },
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    // 注意颜色写的位置
    color: [
      "#006cff",
      "#60cda0",
      "#ed8884",
      "#ff9f7f",
      "#0096ff",
      "#9fe6b8",
      "#32c5e9",
      "#1d9dff"
    ],
    series: [
      {
        name: "COGS by BU",
        type: "pie",
        // 如果radius是百分比则必须加引号
        radius: ["10%", "70%"],
        center: ["50%", "42%"],
        roseType: "radius",
        data: array,
        // 修饰饼形图文字相关的样式 label对象
        label: {
          fontSize: 15,
          formatter: "{b}:{d}%",
        },
        // 修饰引导线样式
        labelLine: {
          // 连接到图形的线长度
          length: 7,
          // 连接到文字的线长度
          length2: 10
        }
      }
    ]
  };

  // 3. 配置项和数据给我们的实例化对象
  myChart.setOption(option);
  // 4. 当我们浏览器缩放的时候，图表也等比例缩放
  window.addEventListener("resize", function() {
    // 让我们的图表调用 resize这个方法
    myChart.resize();
  });
})();

// Project Num by BU
(function() {
  // 1. 实例化对象
  var myChart = echarts.init(document.querySelector(".pie1  .chart"));
  var ctx = document.querySelector(".pie1 .chart");
  var myBUs = ctx.attributes['myBUs'].value;
  var mydata = ctx.attributes['mydata'].value;
  //类型转换
  // console.log(myBUs)
  // console.log(mydata)
  var myBUs = eval(myBUs);
  var mydata = eval(mydata);
  var i = 0;
//构造data数据
len = mydata.length;
var array = [];
for(;i<len;i++){
    array.push({value:mydata[i],name:myBUs[i]});
};
  // 2. 指定配置项和数据
  var option = {
    legend: {
      top: "90%",
      itemWidth: 10,
      itemHeight: 10,
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: 10
      }
    },
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b} : {c} ({d}%)",
    },
    // 注意颜色写的位置
    color: [
      "#006cff",
      "#60cda0",
      "#ed8884",
      "#ff9f7f",
      "#0096ff",
      "#9fe6b8",
      "#32c5e9",
      "#1d9dff"
    ],
    series: [
      {
        name: "Projects by BU",
        type: "pie",
        // 如果radius是百分比则必须加引号
        radius: ["10%", "70%"],
        center: ["50%", "42%"],
        roseType: "radius",
        data: array,
        // 修饰饼形图文字相关的样式 label对象
        label: {
          fontSize: 12,
          formatter: "{b}:{d}%",
        },
        // 修饰引导线样式
        labelLine: {
          // 连接到图形的线长度
          length: 5,
          // 连接到文字的线长度
          length2: 5
        }
      }
    ]
  };

  // 3. 配置项和数据给我们的实例化对象
  myChart.setOption(option);
  // 4. 当我们浏览器缩放的时候，图表也等比例缩放
  window.addEventListener("resize", function() {
    // 让我们的图表调用 resize这个方法
    myChart.resize();
  });
})();

// Project Num by type
(function() {
  // 1. 实例化对象
  var myChart = echarts.init(document.querySelector(".pie2  .chart"));
  var ctx = document.querySelector(".pie2 .chart");
  var myBUs = ctx.attributes['mytypes'].value;
  var mydata = ctx.attributes['mydata'].value;
  //类型转换
  var myBUs = eval(myBUs);
  var mydata = eval(mydata);
  var i = 0;
//构造data数据
len = mydata.length;
var array = [];
for(;i<len;i++){
    array.push({value:mydata[i],name:myBUs[i]});
};
  // 2. 指定配置项和数据
  var option = {
    legend: {
      top: "90%",
      itemWidth: 10,
      itemHeight: 10,
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: 10
      }
    },
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    // 注意颜色写的位置
    color: [
      "#006cff",
      "#60cda0",
      "#ed8884",
      "#ff9f7f",
      "#0096ff",
      "#9fe6b8",
      "#32c5e9",
      "#1d9dff"
    ],
    series: [
      {
        name: "Projects by type",
        type: "pie",
        // 如果radius是百分比则必须加引号
        radius: ["10%", "70%"],
        center: ["50%", "42%"],
        roseType: "radius",
        data: array,
        // 修饰饼形图文字相关的样式 label对象
        label: {
          fontSize: 12,
          formatter: "{b}:{d}%",
        },
        // 修饰引导线样式
        labelLine: {
          // 连接到图形的线长度
          length: 5,
          // 连接到文字的线长度
          length2: 5
        }
      }
    ]
  };

  // 3. 配置项和数据给我们的实例化对象
  myChart.setOption(option);
  // 4. 当我们浏览器缩放的时候，图表也等比例缩放
  window.addEventListener("resize", function() {
    // 让我们的图表调用 resize这个方法
    myChart.resize();
  });
})();

// Project Num by stage
(function() {
  // 1. 实例化对象
  var myChart = echarts.init(document.querySelector(".pie3  .chart"));
  var ctx = document.querySelector(".pie3 .chart");
  var myBUs = ctx.attributes['mystatus'].value;
  var mydata = ctx.attributes['mydata'].value;

  //类型转换
  var myBUs = eval(myBUs);
  var mydata = eval(mydata);
  var i = 0;
//构造data数据
len = mydata.length;
var array = [];
for(;i<len;i++){
    array.push({value:mydata[i],name:myBUs[i]});
};
//  console.log(array)
//  console.log(myBUs)
  // 2. 指定配置项和数据
  var option = {
    legend: {
      top: "90%",
      itemWidth: 10,
      itemHeight: 10,
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "12"
      }
    },
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    // 注意颜色写的位置
    color: [
      "#006cff",
      "#60cda0",
      "#ed8884",
      "#ff9f7f",
      "#0096ff",
      "#9fe6b8",
      "#32c5e9",
      "#1d9dff"
    ],
    series: [
      {
        name: "Projects by status",
        type: "pie",
        // 如果radius是百分比则必须加引号
        radius: ["10%", "70%"],
        center: ["50%", "42%"],
        roseType: "radius",
        data: array,
        // 修饰饼形图文字相关的样式 label对象
        label: {
          fontSize: 12,
          formatter: "{b}:{d}%",
        },
        // 修饰引导线样式
        labelLine: {
          // 连接到图形的线长度
          length: 10,
          // 连接到文字的线长度
          length2: 10
        }
      }
    ]
  };

  // 3. 配置项和数据给我们的实例化对象
  myChart.setOption(option);
  // 4. 当我们浏览器缩放的时候，图表也等比例缩放
  window.addEventListener("resize", function() {
    // 让我们的图表调用 resize这个方法
    myChart.resize();
  });
})();

// Project Num by region
(function() {
  // 1. 实例化对象
  var myChart = echarts.init(document.querySelector(".pie4  .chart"));
  var ctx = document.querySelector(".pie4 .chart");
  var myBUs = ctx.attributes['myregion'].value;
  var mydata = ctx.attributes['mydata'].value;

  //类型转换
  var myBUs = eval(myBUs);
  var mydata = eval(mydata);
  var i = 0;
//构造data数据
len = mydata.length;
var array = [];
for(;i<len;i++){
    array.push({value:mydata[i],name:myBUs[i]});
};
  // console.log(array)
  // console.log(myBUs)
  // 2. 指定配置项和数据
  var option = {
    legend: {
      top: "90%",
      itemWidth: 10,
      itemHeight: 10,
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "12"
      }
    },
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    // 注意颜色写的位置
    color: [
      "#006cff",
      "#60cda0",
      "#ed8884",
      "#ff9f7f",
      "#0096ff",
      "#9fe6b8",
      "#32c5e9",
      "#1d9dff"
    ],
    series: [
      {
        name: "Projects by status",
        type: "pie",
        // 如果radius是百分比则必须加引号
        radius: ["10%", "70%"],
        center: ["50%", "42%"],
        roseType: "radius",
        data: array,
        // 修饰饼形图文字相关的样式 label对象
        label: {
          fontSize: 12,
          formatter: "{b}:{d}%",
        },
        // 修饰引导线样式
        labelLine: {
          // 连接到图形的线长度
          length: 10,
          // 连接到文字的线长度
          length2: 10
        }
      }
    ]
  };

  // 3. 配置项和数据给我们的实例化对象
  myChart.setOption(option);
  // 4. 当我们浏览器缩放的时候，图表也等比例缩放
  window.addEventListener("resize", function() {
    // 让我们的图表调用 resize这个方法
    myChart.resize();
  });
})();

