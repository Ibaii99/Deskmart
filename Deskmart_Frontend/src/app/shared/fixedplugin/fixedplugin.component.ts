import { Component, OnInit } from '@angular/core';

@Component({
    moduleId: module.id,
    selector: 'fixedplugin-cmp',
    templateUrl: 'fixedplugin.component.html'
})

export class FixedPluginComponent implements OnInit{

  public sidebarColor: string = "white";
  public sidebarActiveColor: string = "danger";
  public backgroundActiveColor: string = "default";

  public state: boolean = true;

  changeSidebarColor(color){
    var sidebar = <HTMLElement>document.querySelector('.sidebar');

    this.sidebarColor = color;
    if(sidebar != undefined){
        sidebar.setAttribute('data-color',color);
    }
  }
  changeSidebarActiveColor(color){
    var sidebar = <HTMLElement>document.querySelector('.sidebar');
    this.sidebarActiveColor = color;
    if(sidebar != undefined){
        sidebar.setAttribute('data-active-color',color);
    }
  }
  changeBackgroundActiveColor(color){
    var sidebar = <HTMLElement>document.querySelector('.main-panel');
    this.backgroundActiveColor = color;
    if(sidebar != undefined){
        sidebar.setAttribute('background-color',color);
    }
  }
  ngOnInit(){}
}
