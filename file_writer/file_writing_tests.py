import unittest
import file_writer.file_writing as fw
import file_reader.text_file_reader as tfr


class MyTestCase(unittest.TestCase):

    ##############################   Txt Files   ##############################
    def test_write_txt_small(self):
        # Tests to see that a txt file has been written correctly
        filename = 'txt_small'
        fw.save_formatted_file(small_text, filename, 'txt', "output/")
        output_path = get_output_path(filename, 'txt', "output/")
        if small_text not in tfr.read_txt_file(output_path):
            assert False


    def test_write_txt_large(self):
        # Tests to see that a large txt file has been written correctly
        filename = 'txt_large'
        fw.save_formatted_file(large_text, filename, 'txt', "output/")
        output_path = get_output_path(filename, 'txt', "output/")
        if large_text not in tfr.read_txt_file(output_path):
            assert False


    def test_write_txt_paragraphs(self):
        # Tests to see that multiple paragraphs can be written to a txt file correctly
        filename = 'txt_paragraphs'
        fw.save_formatted_file(paragraphs_text, filename, 'txt', "output/")
        output_path = get_output_path(filename, 'txt', "output/")
        if paragraphs_text not in tfr.read_txt_file(output_path):
            assert False


    ##############################   Pdf Files   ##############################

    def test_write_pdf_small(self):
        # Tests to see that a pdf file has been written correctly
        filename = 'pdf_small'
        fw.save_formatted_file(small_text, filename, 'pdf', "output/")
        output_path = get_output_path(filename, 'pdf', "output/")
        if small_text not in tfr.read_pdf_file(output_path):
            assert False

    def test_write_pdf_paragraphs(self):
        # Tests to see that a pdf has been written to correctly
        # Have to test this differently due to hidden whitespace
        filename = 'pdf_paragraphs'
        fw.save_formatted_file(paragraphs_text, filename, 'pdf', "output/")
        output_path = get_output_path(filename, 'pdf', "output/")
        to_test = "".join(paragraphs_text.split(" "))
        testing = "".join(tfr.read_pdf_file(output_path).split(" "))
        self.assertEqual(testing, to_test)


    ##############################   Docx Files   ##############################

    def test_write_docx_small(self):
        # Tests to see that a small docx file has been written to correctly
        filename = 'docx_small'
        fw.save_formatted_file(small_text, filename, 'docx', "output/")
        output_path = get_output_path(filename, 'docx', "output/")
        if small_text not in tfr.read_docx_file(output_path):
            assert False


    def test_write_docx_large(self):
        # Tests to see that a large docx file has been written to correctly
        filename = 'docx_large'
        fw.save_formatted_file(large_text, filename, 'docx', "output/")
        output_path = get_output_path(filename, 'docx', "output/")
        if large_text not in tfr.read_docx_file(output_path):
            assert False

    def test_write_docx_paragraphs(self):
        # Tests to see that a docx file with paragraphs has been written to correctly
        filename = 'docx_paragraphs'
        fw.save_formatted_file(paragraphs_text, filename, 'docx', "output/")
        output_path = get_output_path(filename, 'docx', "output/")
        if paragraphs_text not in tfr.read_docx_file(output_path):
            assert False


if __name__ == '__main__':
    unittest.main()


def get_output_path(file_name, extension, path):
    # Gets the output path for a file
    return path + file_name + "." + extension


small_text = "Hello World!"

paragraphs_text = """This is the first paragraph

This is the next paragraph

This is the third paragraph"""

large_text = """This file will be cluttered with lorem ipsum text to make it take enough space to be considered a large file:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus dictum feugiat tortor et aliquam. Donec suscipit a felis in molestie. Maecenas tincidunt diam quis lobortis luctus. Aenean cursus felis vitae ex fermentum, vitae mattis nunc sagittis. Donec varius et augue eu porta. Vivamus dictum ipsum cursus massa sagittis, et feugiat ligula ornare. Aliquam id dapibus eros, sed fermentum lacus. Sed quis placerat nulla. Donec interdum maximus nunc.

Nulla dignissim quis risus congue sollicitudin. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque fermentum at est ac volutpat. Vivamus varius vulputate sodales. Cras a interdum odio, et aliquet est. Nulla elementum ante quis ligula fermentum, vitae bibendum orci scelerisque. Quisque at velit ligula. Nam auctor nunc non dolor elementum, ac aliquam eros hendrerit. Nulla in lacus id purus tristique varius.

Sed sed ante lacus. Aenean rhoncus dui massa, imperdiet gravida urna ultrices eu. Suspendisse eu posuere lectus. In eget tortor viverra, consectetur nisl egestas, egestas elit. Quisque elementum lorem eget turpis lacinia pellentesque. Fusce sit amet ultrices justo. Quisque mi leo, rhoncus vehicula ex sit amet, rhoncus congue ante. Donec sed pretium odio. Etiam tortor ligula, condimentum a pulvinar gravida, gravida in odio. Nunc molestie blandit lacinia. Nullam imperdiet ipsum risus, ac varius ipsum aliquam non. Fusce vitae velit a ipsum tincidunt auctor. Suspendisse ac dolor quis dolor placerat commodo at vitae enim. Quisque eget ipsum justo. Aenean mollis egestas nulla malesuada sodales.

Praesent blandit sem quis euismod vulputate. Nulla facilisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean ornare, quam eu fringilla mollis, augue arcu viverra enim, mollis eleifend est urna non sapien. Mauris aliquet ultrices turpis, sit amet ornare neque mattis sed. Proin consequat tortor id eros scelerisque iaculis. Nulla placerat ex et tempor dignissim. Morbi at semper felis. Sed quis est massa. Aliquam pretium nunc nisl, vitae sollicitudin lorem venenatis cursus. Ut interdum, risus a aliquam imperdiet, odio ligula faucibus urna, eu interdum risus magna pulvinar purus. Nunc vestibulum ex id interdum molestie. Nulla ut dui luctus, suscipit nunc vitae, porttitor lorem. Fusce eget mauris lacus.

Nam neque elit, venenatis id nunc et, dictum molestie odio. Morbi in laoreet orci. Donec ac mattis ligula. Nam pharetra urna tellus, vitae dictum eros consequat et. Curabitur ac eros eget elit pretium feugiat eget a nibh. Sed placerat placerat turpis, et tempor arcu pulvinar et. Pellentesque at convallis ligula. Mauris vel sodales est. Morbi hendrerit fermentum dolor, et porta quam ultricies eget.

Mauris accumsan nunc magna, ut mattis est pretium sed. Ut blandit eu est ut dignissim. Morbi accumsan lobortis purus at congue. In id faucibus mauris. Nulla scelerisque tempor finibus. Nam in libero id leo sollicitudin euismod. Vestibulum quis sodales nulla.

Pellentesque eros libero, tristique et tortor sit amet, viverra facilisis felis. Morbi id vestibulum ipsum. Morbi enim velit, volutpat vitae semper et, accumsan vitae erat. Etiam nec dui quis eros sollicitudin pharetra. Sed nec orci fringilla erat fringilla sodales sed id leo. Mauris convallis lobortis quam, ac accumsan metus mollis vel. Phasellus semper volutpat urna nec consectetur. Proin tempus erat ut efficitur ultricies. Nulla porttitor dolor et ipsum maximus, sit amet pellentesque nulla ultrices. Proin in ligula lacus. Aliquam mollis ex nulla, id molestie ipsum pharetra eu. Integer sed mi pulvinar, pulvinar ipsum in, vehicula purus. Nullam in ipsum tellus. Suspendisse tincidunt congue leo, non pharetra nunc finibus vel. Nulla ultricies, nisl ullamcorper tincidunt ornare, neque metus mollis augue, a scelerisque sem justo sit amet est.

Praesent tempor vehicula orci, non fringilla dolor ullamcorper a. Integer dapibus convallis diam, id lacinia elit posuere vitae. Aenean vitae risus quis orci sollicitudin ultricies. Nunc fringilla porttitor sagittis. In in justo eget odio placerat tempus a eget nisl. Suspendisse sed dapibus nulla. Phasellus placerat vel metus eu ultrices. Sed et pretium mauris, in scelerisque enim. Vivamus porttitor porttitor nunc a ornare. Ut nec facilisis sem. Maecenas condimentum lorem consectetur lorem mattis tempor. Nam a quam eu nibh congue faucibus. Sed sodales dolor quis mauris egestas, vitae semper augue convallis. Aliquam lacus nisl, maximus ac urna sed, interdum eleifend nulla.

Vestibulum vitae orci et dolor semper tincidunt sit amet vel ipsum. Aenean dictum fermentum urna eget convallis. Aenean vel venenatis libero. Praesent vel rhoncus neque. Nullam pulvinar, mi ut molestie bibendum, neque lacus dapibus lectus, et rhoncus urna sapien vestibulum dolor. Donec blandit semper sapien sed euismod. Mauris vel venenatis est. Donec ut volutpat dolor, sed hendrerit risus. Quisque efficitur non tellus in suscipit. Cras sed tellus tincidunt, vestibulum nulla vitae, hendrerit purus. Vivamus vel sollicitudin nulla. Ut lacinia pretium justo, non ultrices lorem egestas quis. Suspendisse et mi leo. Quisque aliquet ultricies augue, non accumsan libero sollicitudin ut.

Duis id auctor ante. Nullam a nisl vitae lectus placerat faucibus. Cras rutrum imperdiet pharetra. Maecenas ornare lobortis velit, tristique malesuada ligula feugiat sit amet. Phasellus efficitur ante ac posuere sollicitudin. Interdum et malesuada fames ac ante ipsum primis in faucibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur sagittis posuere mi nec semper. Proin sit amet nisi ac ex euismod posuere sed vel felis. Etiam feugiat lectus ac purus facilisis, at tempor nunc elementum. Phasellus commodo quam sit amet maximus fringilla. Sed at tellus bibendum neque luctus bibendum quis vel risus. Maecenas ut ipsum placerat, ornare nisi a, porta metus. Nullam porttitor sagittis tellus, vitae molestie mauris convallis dictum.

Nam convallis, leo eu rhoncus mattis, ligula mauris imperdiet erat, a vulputate lacus justo vitae ipsum. Maecenas nec venenatis eros. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam hendrerit mauris quis auctor scelerisque. In hac habitasse platea dictumst. Vestibulum non elit ullamcorper, varius ex semper, mollis lectus. Duis mattis urna sed tellus fringilla ultricies.

Nunc ut justo mauris. Quisque eu sem eget elit mattis rhoncus. Aenean eu tempor ex. Quisque rhoncus a augue in dictum. Ut eu vehicula est, non volutpat libero. Vestibulum lectus enim, bibendum ut nulla vel, finibus accumsan risus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Phasellus egestas pretium neque, nec elementum lectus. Nulla ut mi neque. Proin gravida nisi in eleifend faucibus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam sit amet odio ultricies metus laoreet condimentum. Ut consequat eu mauris ac scelerisque. Vestibulum accumsan, nisi in cursus finibus, lacus tellus cursus orci, vitae gravida purus dolor quis odio. Sed blandit quam porttitor pretium tincidunt. Praesent massa felis, tempus vitae lobortis sed, dignissim vitae sem.

Vestibulum volutpat consequat elit sit amet lobortis. Nam eget elit lectus. Nullam cursus imperdiet mi a egestas. Donec pellentesque urna ut eros ultrices, at pretium urna gravida. Donec hendrerit iaculis urna eu rhoncus. Vestibulum vitae nulla eu lorem commodo aliquam. Quisque rutrum, leo vitae molestie maximus, dui ligula rhoncus ex, hendrerit facilisis nisi leo sed lacus. Integer non sollicitudin dolor. Phasellus pharetra porta metus, non lacinia ligula condimentum quis. Proin nec facilisis orci, sed tempor tortor. Nunc facilisis purus ac nulla laoreet lacinia. Nullam fermentum a purus malesuada ultricies. Morbi nec felis sit amet mauris condimentum ullamcorper. In a cursus dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Quisque sed pulvinar tortor. Suspendisse sit amet tellus id justo cursus pharetra. Curabitur imperdiet sit amet quam non rutrum. Curabitur vehicula malesuada magna, feugiat consectetur metus semper elementum. In sed velit enim. Phasellus mattis leo sit amet nisi ornare aliquet. Nullam imperdiet fringilla orci nec vulputate. Phasellus neque nunc, hendrerit eu tincidunt a, semper cursus nunc. Praesent dictum, odio sodales posuere congue, neque magna luctus nunc, non dapibus urna est et mauris. Nullam cursus finibus sapien nec hendrerit. Phasellus quis facilisis lorem, non porttitor felis. Donec vel fermentum est. Mauris convallis arcu velit. Integer finibus enim ut nisl aliquam, id laoreet lorem vestibulum.

Mauris feugiat id ante ac sollicitudin. In ut nibh a libero convallis rhoncus. Integer lorem tellus, euismod eu tincidunt ac, efficitur quis ipsum. Nunc a augue sed ipsum posuere vulputate ut non tortor. Nam eu risus et lorem maximus rutrum rutrum et diam. Maecenas vehicula id urna a tristique. Nulla malesuada ac tellus vitae porttitor. Quisque in turpis purus. Phasellus accumsan ante ac velit ullamcorper tempor. Nulla dapibus ut nulla non faucibus. Morbi nisi quam, vehicula et ipsum eu, ultricies viverra massa. Praesent tempus mattis enim ac hendrerit. Nulla facilisi. Nulla facilisi. Curabitur accumsan sollicitudin urna, quis imperdiet dui sagittis aliquet.

Duis semper finibus egestas. Morbi ipsum quam, scelerisque at pharetra quis, sollicitudin sit amet velit. Suspendisse consectetur sollicitudin nisi. Praesent iaculis volutpat diam sit amet elementum. Praesent malesuada suscipit arcu, eu finibus leo pharetra nec. Phasellus accumsan eros ac libero malesuada varius. Cras facilisis venenatis mollis. Mauris efficitur non nisl sed efficitur. Sed sem quam, consequat eget tortor nec, cursus mollis sapien.

Nam venenatis interdum neque, vel sollicitudin metus tempor in. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam in nisi quis odio dignissim laoreet. In vel accumsan dolor. Pellentesque ante nisi, elementum quis tempus ut, accumsan eget nisl. Nulla facilisi. Sed eu est vitae magna placerat euismod. Integer molestie enim vitae tortor ultricies, vel facilisis odio eleifend. Sed in mi in est aliquet hendrerit. Vivamus sit amet turpis purus. Vivamus iaculis risus nisi, non pharetra risus pretium elementum. Phasellus sed felis vitae ante malesuada interdum. Duis vitae placerat leo. Suspendisse sagittis aliquam augue in lacinia. Duis maximus cursus leo non euismod.

reached the end properly
"""