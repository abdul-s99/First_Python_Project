import ExcelLoader as el


class Header(object):
    def __init__(self, company, project, floor, location, date, page_text, contractor, frame, coordinator):
        self.company = company
        self.project = project
        self.floor = floor
        self.location = location
        self.date = date
        self.page_text = page_text
        self.contractor = contractor
        self.frame = frame
        self.coordinator = coordinator

    # use this to debug data source and why values might not be working, is called representation unique to above class
    def __repr__(self):
        return f"{self.company} x {self.project},Tag: {self.floor},Panel: {self.contractor}"


class PageSetup:
    def __init__(self, pdf_file, pdf_path):
        self.pdf_file = pdf_file
        self.pdf_path = pdf_path
        self.height = 793
        self.width = 615
        self.x_origin = 0
        self.y_origin = 0

    def generate_page(self, c, imagePaths, imageSizes, imagePositions):
        cutoutImageX = self.x_origin + 30
        cutoutImageY = self.y_origin + 40

        c.setFont("Helvetica", 12)
        Excel = el.CSVtoARRAY(self.pdf_path)

        c.drawImage("THP_Template.png", self.x_origin, self.y_origin, self.width, self.height)

        currentHeader = Header(Excel.array[0][0], Excel.array[0][2], Excel.array[0][1],
                               "388 Applewood Cres TORO", "2023-10-25", "1 of 1",
                               "ABDUL AND SAI", "258T", "COORD")

        currentLocation = currentHeader.location
        currentJobName = currentHeader.project
        currentFloorNumber = currentHeader.floor
        currentDate = currentHeader.date
        currentPageText = currentHeader.page_text
        currentContractor = currentHeader.contractor
        currentFrame = currentHeader.frame
        currentCoordinator = currentHeader.coordinator

        text_info = [(currentLocation, self.x_origin + 85, self.height - 105),
                     (currentJobName, self.x_origin + 215, self.height - 40),
                     (currentFloorNumber, self.x_origin + 200, self.height - 75),
                     (currentDate, self.x_origin + 475, self.height - 65),
                     (currentPageText, self.x_origin + 475, self.height - 85),
                     (currentContractor, self.x_origin + 100, self.height - 125),
                     (currentFrame, self.x_origin + 485, self.height - 105),
                     (currentCoordinator, self.x_origin + 495, self.height - 127)
                     ]

        for text in text_info:
            c.drawString(text[1], text[2], text[0])

        for i in range(len(imagePaths)):
            image_path = imagePaths[i]
            image_size = imageSizes[0]
            image_position = (imagePositions[i][0], imagePositions[i][1])
            c.drawImage(image_path, *image_position, *image_size)
        c.save()


class ThpItem(object):
    def __init__(self, thp_type, panel_width: float, panel_height: float, tag: str, cut_out_list):
        self.width = panel_width
        self.height = panel_height
        self.thp_type = thp_type
        self.tag = tag
        self.cut_out_list = cut_out_list


class CutoutDetail(object):
    def __init__(self, shape, x_location, y_location, height, width):
        self.shape = shape
        self.xLocation = x_location
        self.yLocation = y_location
        self.height = height
        self.width = width


def tagpopulator():
    pass
    # Determine the number of tags to display on this page


class ItemContainer(object):
    def __init__(self, thp_items, item_container_position, pagenumber):
        self.thp_items = thp_items
        self.item_container_position = item_container_position
        self.pagenumber = pagenumber
        self.cutoutdescr = ""
        self.item_picture_x = 100
        self.item_picture_y = 500
        self.item_picture_height = 180
        self.item_picture_width = 300


class Footer(object):
    def __init__(self, xloc, yloc, page_text):
        self.xloc = xloc
        self.yloc = yloc
        self.page_text = page_text


class PageSet(object):
    def __init__(self, pdf_file, pdf_path):
        self.pdf_file = pdf_file
        self.pdf_path = pdf_path
        self.height = 793
        self.width = 615
        self.x_origin = 0
        self.y_origin = 0
