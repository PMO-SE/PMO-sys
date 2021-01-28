// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('main'));

// 指定图表的配置项和数据
var option = {
    series: [{
        type: 'treemap',
        data: [{
            name: 'nodeA',            // First tree
            value: 10,
            children: [{
                name: 'nodeAa',       // First leaf of first tree
                value: 4
            }, {
                name: 'nodeAb',       // Second leaf of first tree
                value: 6
            }]
        }, {
            name: 'nodeB',            // Second tree
            value: 20,
            children: [{
                name: 'nodeBa',       // Son of first tree
                value: 20,
                children: [{
                    name: 'nodeBa1',  // Granson of first tree
                    value: 20
                }]
            }]
        }]
    }]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);