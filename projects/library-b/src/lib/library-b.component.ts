import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'lib-library-b',
  template: `
    <p>
      library-b works!
    </p>
  `,
  styles: [
  ]
})
export class LibraryBComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

}
