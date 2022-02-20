arr = ['aaa,aaa', 'bbb,bb', 'cccc', 'dd,dd,']
// arr.shift()
newarr = []
arr.forEach(element => {



    newarr.push(element.replace(',', ''))


    console.log('Element;', element)
    console.log(newarr)
    // return element

});
