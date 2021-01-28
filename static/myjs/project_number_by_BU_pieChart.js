// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myBUs = ctx.attributes['myBUs'].value
var mydata = ctx.attributes['mydata'].value
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: myBUs ,
    datasets: [{
      data: mydata ,

    }],
  },
  options: {},
});

