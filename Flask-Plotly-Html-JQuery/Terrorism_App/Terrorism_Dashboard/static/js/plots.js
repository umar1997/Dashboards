$(document).ready(function() {
  $('#plot_type').on('change',function(){
      var url = "http://localhost:5000/charts"
      $.ajax({
          url: url,
          type: "GET",
          contentType: 'application/json;charset=UTF-8',
          data: {
              'selected': document.getElementById('plot_type').value

          },
          dataType:"json",
          success: function (data) {
              Plotly.newPlot('firstgraph', data );
          }
      });
  });
  $('#time_frame').on('change',function(){
      var url = "http://localhost:5000/series"
      $.ajax({
          url: url,
          type: "GET",
          contentType: 'application/json;charset=UTF-8',
          data: {
              'time_selected': document.getElementById('time_frame').value,
              'country_selected': document.getElementById('country_frame').value

          },
          dataType:"json",
          success: function (data) {
              Plotly.newPlot('time-graph',
              data.data,
              data.layout || {} );
          }
      });
  });
  $('#country_frame').on('change',function(){
      var url = "http://localhost:5000/series"
      $.ajax({
          url: url,
          type: "GET",
          contentType: 'application/json;charset=UTF-8',
          data: {
              'time_selected': document.getElementById('time_frame').value,
              'country_selected': document.getElementById('country_frame').value

          },
          dataType:"json",
          success: function (data) {
              Plotly.newPlot('time-graph',
              data.data,
              data.layout || {} );
          }
      });
      console.log(document.getElementById('country_frame').value)
  });



});
