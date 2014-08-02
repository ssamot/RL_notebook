% Metapost TeX macro
% Title: /home/ssamot/projects/teaching/CE802/RL/MDPExample.dia
% Creator: Dia v0.97.2
% CreationDate: Sat Aug  2 10:47:22 2014
% For: ssamot


beginfig(1);
verbatimtex
%&latex
\documentclass{minimal}
\begin{document}
etex
% Define macro for horizontal centering.
vardef hcentered primary P =
  P shifted -(xpart center P, 0)
enddef;
% Define macro for right justification.
vardef rjust primary P =
  P shifted -(xpart (lrcorner P - llcorner P), 0)
enddef;
  % picture(15.805000,-28.785000)(52.545000,-6.352500)
  x = 1.000000cm; y = -1.000000cm;

  t = 1.000000;

% set_line_color 0.000000, 0.000000, 0.000000
% set_line_color 1.000000, 1.000000, 1.000000
% set_linewidth 0.100000
% set_linewidth 0.100000
  path p;
  p = (37.562500x,17.537500y)..(34.075000x,21.025000y)..(30.587500x,17.537500y)..(34.075000x,14.050000y)..cycle;
  fill p withcolor (1.000000,1.000000,1.000000);
% set_line_color 0.000000, 0.000000, 0.000000
  draw (37.562500x,17.537500y)..(34.075000x,21.025000y)..(30.587500x,17.537500y)..(34.075000x,14.050000y)..cycle
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw (37.562500x,17.537500y)..(34.075000x,21.025000y)..(30.587500x,17.537500y)..(34.075000x,14.050000y)..cycle
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw hcentered btex {\usefont{OT1}{phv}{m}{n} Flying} etex scaled 1.64t shifted (34.075000x,17.537500y);
% set_line_color 0.000000, 0.000000, 0.000000
  draw hcentered btex {\usefont{OT1}{phv}{m}{n} R = 0} etex scaled 1.64t shifted (34.075000x,18.337500y);
% set_linewidth 0.100000
% set_linewidth 0.100000
  path p;
  p = (28.775000x,17.537500y)..(26.462500x,19.850000y)..(24.150000x,17.537500y)..(26.462500x,15.225000y)..cycle;
  fill p withcolor (1.000000,1.000000,1.000000);
% set_line_color 0.000000, 0.000000, 0.000000
  draw (28.775000x,17.537500y)..(26.462500x,19.850000y)..(24.150000x,17.537500y)..(26.462500x,15.225000y)..cycle
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw (28.775000x,17.537500y)..(26.462500x,19.850000y)..(24.150000x,17.537500y)..(26.462500x,15.225000y)..cycle
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw hcentered btex {\usefont{OT1}{phv}{m}{n} Attack_Turtle} etex scaled 1.64t shifted (26.462500x,17.537500y);
% set_linewidth 0.100000
% set_linewidth 0.100000
  path p;
  p = (44.105000x,17.537500y)..(41.792500x,19.850000y)..(39.480000x,17.537500y)..(41.792500x,15.225000y)..cycle;
  fill p withcolor (1.000000,1.000000,1.000000);
% set_line_color 0.000000, 0.000000, 0.000000
  draw (44.105000x,17.537500y)..(41.792500x,19.850000y)..(39.480000x,17.537500y)..(41.792500x,15.225000y)..cycle
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw (44.105000x,17.537500y)..(41.792500x,19.850000y)..(39.480000x,17.537500y)..(41.792500x,15.225000y)..cycle
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw hcentered btex {\usefont{OT1}{phv}{m}{n} Attack_Boar} etex scaled 1.64t shifted (41.792500x,17.537500y);
% set_linewidth 0.100000
% set_linewidth 0.100000
  path p;
  p = (23.030000x,9.890000y)..(19.542500x,13.377500y)..(16.055000x,9.890000y)..(19.542500x,6.402500y)..cycle;
  fill p withcolor (1.000000,1.000000,1.000000);
% set_line_color 0.000000, 0.000000, 0.000000
  draw (23.030000x,9.890000y)..(19.542500x,13.377500y)..(16.055000x,9.890000y)..(19.542500x,6.402500y)..cycle
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw (23.030000x,9.890000y)..(19.542500x,13.377500y)..(16.055000x,9.890000y)..(19.542500x,6.402500y)..cycle
    withpen pencircle scaled 0.1000x;
% set_linewidth 0.100000
% set_linewidth 0.100000
  path p;
  p = (52.095000x,9.890000y)..(48.607500x,13.377500y)..(45.120000x,9.890000y)..(48.607500x,6.402500y)..cycle;
  fill p withcolor (1.000000,1.000000,1.000000);
% set_line_color 0.000000, 0.000000, 0.000000
  draw (52.095000x,9.890000y)..(48.607500x,13.377500y)..(45.120000x,9.890000y)..(48.607500x,6.402500y)..cycle
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw (52.095000x,9.890000y)..(48.607500x,13.377500y)..(45.120000x,9.890000y)..(48.607500x,6.402500y)..cycle
    withpen pencircle scaled 0.1000x;
% set_linewidth 0.100000
% set_linewidth 0.100000
  path p;
  p = (22.830000x,25.247500y)..(19.342500x,28.735000y)..(15.855000x,25.247500y)..(19.342500x,21.760000y)..cycle;
  fill p withcolor (1.000000,1.000000,1.000000);
% set_line_color 0.000000, 0.000000, 0.000000
  draw (22.830000x,25.247500y)..(19.342500x,28.735000y)..(15.855000x,25.247500y)..(19.342500x,21.760000y)..cycle
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw (22.830000x,25.247500y)..(19.342500x,28.735000y)..(15.855000x,25.247500y)..(19.342500x,21.760000y)..cycle
    withpen pencircle scaled 0.1000x;
% set_linewidth 0.100000
% set_linewidth 0.100000
  path p;
  p = (52.495000x,25.247500y)..(49.007500x,28.735000y)..(45.520000x,25.247500y)..(49.007500x,21.760000y)..cycle;
  fill p withcolor (1.000000,1.000000,1.000000);
% set_line_color 0.000000, 0.000000, 0.000000
  draw (52.495000x,25.247500y)..(49.007500x,28.735000y)..(45.520000x,25.247500y)..(49.007500x,21.760000y)..cycle
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw (52.495000x,25.247500y)..(49.007500x,28.735000y)..(45.520000x,25.247500y)..(49.007500x,21.760000y)..cycle
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw hcentered btex {\usefont{OT1}{phv}{m}{n} Turtle_Grabbed} etex scaled 1.64t shifted (19.542500x,9.890000y);
% set_line_color 0.000000, 0.000000, 0.000000
  draw hcentered btex {\usefont{OT1}{phv}{m}{n} R = 3} etex scaled 1.64t shifted (19.542500x,10.690000y);
% set_line_color 0.000000, 0.000000, 0.000000
  draw hcentered btex {\usefont{OT1}{phv}{m}{n} } etex scaled 1.64t shifted (19.542500x,11.490000y);
% set_line_color 0.000000, 0.000000, 0.000000
  draw hcentered btex {\usefont{OT1}{phv}{m}{n} } etex scaled 1.64t shifted (19.542500x,12.290000y);
% set_linewidth 0.100000
% set_line_color 0.000000, 0.000000, 0.000000
  draw (43.406451x,19.262180y)--(46.257694x,22.309038y)
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
% fill_polygon
  path p;
  p = (46.513924x,22.582847y)--(45.989745x,22.388588y)--(46.257694x,22.309038y)--(46.354823x,22.046948y)--cycle;
  fill p 
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw (46.513924x,22.582847y)--(45.989745x,22.388588y)--(46.257694x,22.309038y)--(46.354823x,22.046948y)--cycle
    withpen pencircle scaled 0.1000x;
% set_linewidth 0.100000
% set_line_color 0.000000, 0.000000, 0.000000
  draw (43.363976x,15.774057y)--(45.929949x,12.894632y)
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
% fill_polygon
  path p;
  p = (46.179438x,12.614667y)--(46.033430x,13.154280y)--(45.929949x,12.894632y)--(45.660143x,12.821628y)--cycle;
  fill p 
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw (46.179438x,12.614667y)--(46.033430x,13.154280y)--(45.929949x,12.894632y)--(45.660143x,12.821628y)--cycle
    withpen pencircle scaled 0.1000x;
% set_linewidth 0.100000
% set_line_color 0.000000, 0.000000, 0.000000
  draw (24.859587x,19.273238y)--(22.072463x,22.291318y)
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
% fill_polygon
  path p;
  p = (21.818049x,22.566814y)--(21.973604x,22.029876y)--(22.072463x,22.291318y)--(22.340933x,22.369095y)--cycle;
  fill p 
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw (21.818049x,22.566814y)--(21.973604x,22.029876y)--(22.072463x,22.291318y)--(22.340933x,22.369095y)--cycle
    withpen pencircle scaled 0.1000x;
% set_linewidth 0.100000
% set_line_color 0.000000, 0.000000, 0.000000
  draw (24.877371x,15.785726y)--(22.241961x,12.873256y)
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
% fill_polygon
  path p;
  p = (21.990352x,12.595195y)--(22.511205x,12.798203y)--(22.241961x,12.873256y)--(22.140457x,13.133682y)--cycle;
  fill p 
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw (21.990352x,12.595195y)--(22.511205x,12.798203y)--(22.241961x,12.873256y)--(22.140457x,13.133682y)--cycle
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw hcentered btex {\usefont{OT1}{phv}{m}{n} Turtle_Escaped} etex scaled 1.64t shifted (19.342500x,25.247500y);
% set_line_color 0.000000, 0.000000, 0.000000
  draw hcentered btex {\usefont{OT1}{phv}{m}{n} R = 0} etex scaled 1.64t shifted (19.342500x,26.047500y);
% set_linewidth 0.100000
%metapost_arc
% center->x = 32.170884% center->y = 14.352966% width = 7.420759% height = 7.420759% angle1 = 100.423471% angle2 = 243.970404% set_line_color 0.000000, 0.000000, 0.000000
  draw (31.499594x,10.703817y)..(28.494860x,13.849213y)..(30.542638x,17.686992y)
    withpen pencircle scaled 0.1000x
    dashed dashpattern (on 1.000000x off 1.000000x);
% set_line_color 0.000000, 0.000000, 0.000000
% fill_polygon
  path p;
  p = (31.868345x,10.653252y)--(31.381868x,10.928644y)--(31.493841x,10.672544y)--(31.356145x,10.429306y)--cycle;
  fill p 
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw (31.868345x,10.653252y)--(31.381868x,10.928644y)--(31.493841x,10.672544y)--(31.356145x,10.429306y)--cycle
    withpen pencircle scaled 0.1000x;
% set_linewidth 0.100000
% set_linewidth 0.100000
  path p;
  p = (36.605000x,10.647500y)..(34.292500x,12.960000y)..(31.980000x,10.647500y)..(34.292500x,8.335000y)..cycle;
  fill p withcolor (1.000000,1.000000,1.000000);
% set_line_color 0.000000, 0.000000, 0.000000
  draw (36.605000x,10.647500y)..(34.292500x,12.960000y)..(31.980000x,10.647500y)..(34.292500x,8.335000y)..cycle
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw (36.605000x,10.647500y)..(34.292500x,12.960000y)..(31.980000x,10.647500y)..(34.292500x,8.335000y)..cycle
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw hcentered btex {\usefont{OT1}{phv}{m}{n} Keep_Flying} etex scaled 1.64t shifted (34.292500x,10.647500y);
% set_line_color 0.000000, 0.000000, 0.000000
  draw btex {\usefont{OT1}{phv}{m}{n} } etex scaled 1.64t shifted (34.292500x,10.647500y);
% set_linewidth 0.100000
%metapost_arc
% center->x = 36.340461% center->y = 14.195794% width = 7.116284% height = 7.116284% angle1 = 297.877613% angle2 = 85.736271% set_line_color 0.000000, 0.000000, 0.000000
  draw (38.004193x,17.341008y)..(39.823322x,13.467747y)..(36.605000x,10.647500y)
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
% fill_polygon
  path p;
  p = (37.667503x,17.499101y)--(38.051226x,17.092584y)--(38.019692x,17.370308y)--(38.222950x,17.562170y)--cycle;
  fill p 
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw (37.667503x,17.499101y)--(38.051226x,17.092584y)--(38.019692x,17.370308y)--(38.222950x,17.562170y)--cycle
    withpen pencircle scaled 0.1000x;
% set_linewidth 0.100000
%metapost_arc
% center->x = 30.404036% center->y = 19.139096% width = 8.010265% height = 8.010265% angle1 = 197.154096% angle2 = 331.162966% set_line_color 0.000000, 0.000000, 0.000000
  draw (26.577071x,20.320380y)..(29.996408x,23.123431y)..(33.912512x,21.070851y)
    withpen pencircle scaled 0.1000x
    dashed dashpattern (on 1.000000x off 1.000000x);
% set_line_color 0.000000, 0.000000, 0.000000
% fill_polygon
  path p;
  p = (26.482345x,19.960028y)--(26.817124x,20.407714y)--(26.548907x,20.329073y)--(26.325064x,20.496463y)--cycle;
  fill p 
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw (26.482345x,19.960028y)--(26.817124x,20.407714y)--(26.548907x,20.329073y)--(26.325064x,20.496463y)--cycle
    withpen pencircle scaled 0.1000x;
% set_linewidth 0.100000
%metapost_arc
% center->x = 37.720520% center->y = 19.036990% width = 8.304698% height = 8.304698% angle1 = 208.604942% angle2 = 342.022231% set_line_color 0.000000, 0.000000, 0.000000
  draw (34.075000x,21.025000y)..(38.105056x,23.171495y)..(41.670137x,20.318604y)
    withpen pencircle scaled 0.1000x
    dashed dashpattern (on 1.000000x off 1.000000x);
% set_line_color 0.000000, 0.000000, 0.000000
% fill_polygon
  path p;
  p = (41.770609x,19.959639y)--(41.917873x,20.498911y)--(41.697186x,20.327381y)--(41.427551x,20.401013y)--cycle;
  fill p 
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw (41.770609x,19.959639y)--(41.917873x,20.498911y)--(41.697186x,20.327381y)--(41.427551x,20.401013y)--cycle
    withpen pencircle scaled 0.1000x;
% set_line_color 0.000000, 0.000000, 0.000000
  draw btex {\usefont{OT1}{phv}{m}{n} } etex scaled 1.64t shifted (49.007500x,25.247500y);
% set_line_color 0.000000, 0.000000, 0.000000
  draw hcentered btex {\usefont{OT1}{phv}{m}{n} Boar_Escaped} etex scaled 1.64t shifted (49.007500x,25.247500y);
% set_line_color 0.000000, 0.000000, 0.000000
  draw hcentered btex {\usefont{OT1}{phv}{m}{n} R = 0} etex scaled 1.64t shifted (49.007500x,26.047500y);
% set_line_color 0.000000, 0.000000, 0.000000
  draw hcentered btex {\usefont{OT1}{phv}{m}{n} Boar_Grabbed} etex scaled 1.64t shifted (48.607500x,9.890000y);
% set_line_color 0.000000, 0.000000, 0.000000
  draw hcentered btex {\usefont{OT1}{phv}{m}{n} R = 10} etex scaled 1.64t shifted (48.607500x,10.690000y);
% set_line_color 0.000000, 0.000000, 0.000000
  draw btex {\usefont{OT1}{phv}{m}{n} $\gamma = 0.99$} etex scaled 1.64t shifted (31.550000x,26.900000y);
endfig;
end;
